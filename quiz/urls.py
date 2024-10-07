# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.take_quiz, name='take_quiz'),
    path('result/<int:result_id>/', views.quiz_result, name='quiz_result'),
    path('grafico/', views.grafico_areas, name='grafico_areas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login-redirect/', views.redirecionar_apos_login, name='login_redirect'),
]
