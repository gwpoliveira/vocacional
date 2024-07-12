# quiz/admin.py
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

admin.site.register(Area, AreaAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Result, ResultAdmin)
