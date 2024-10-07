# quiz/admin.py
import pandas as pd
from django.http import HttpResponse
from django.contrib import admin
from .models import Area, Question, Option, Result

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'area')
    list_filter = ('area',)
    search_fields = ('text',)

class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')
    list_filter = ('question',)
    search_fields = ('text',)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_email', 'area', 'score')
    list_filter = ('area', 'score')
    search_fields = ('student_name', 'student_email')
    actions = ['exportar_para_excel']

    def exportar_para_excel(self, request, queryset):
        # Permitir que somente superusuários executem esta ação
        if not request.user.is_superuser:
            self.message_user(request, "Ação não permitida. Somente superusuários podem exportar os dados.", level='error')
            return

        # Gerar o DataFrame com os resultados selecionados, formatando o score para duas casas decimais
        data = {
            'Nome': [resultado.student_name for resultado in queryset],
            'Email': [resultado.student_email for resultado in queryset],
            'Whatsapp': [resultado.whatsapp for resultado in queryset],
            'Escola': [resultado.school_name for resultado in queryset],
            'Área': [resultado.area.name for resultado in queryset],
            'Pontuação': [f'{resultado.score:.2f}' for resultado in queryset],  # Formata o score com duas casas decimais
        }
        df = pd.DataFrame(data)

        # Configurar a resposta para download do Excel
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="resultados.xlsx"'
        df.to_excel(response, index=False)

        return response

    exportar_para_excel.short_description = "Exportar resultados selecionados para Excel"

admin.site.register(Area, AreaAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Result, ResultAdmin)
