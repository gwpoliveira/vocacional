from django.urls import path
from . import views

urlpatterns = [
    path('', views.take_quiz, name='take_quiz'),  # URL para iniciar o quiz
    path('result/<int:result_id>/', views.quiz_result, name='quiz_result'),  # URL para mostrar o resultado
]