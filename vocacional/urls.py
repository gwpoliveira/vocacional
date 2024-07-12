from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Adiciona a URL para a página inicial
    path('quiz/', include('quiz.urls')),
]
