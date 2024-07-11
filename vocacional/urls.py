from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # URL para a página inicial
    path('quiz/', include('quiz.urls')),  # Inclui as URLs do app 'quiz'
]
