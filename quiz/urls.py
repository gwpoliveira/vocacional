# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.take_quiz, name='take_quiz'),
    path('result/<int:result_id>/', views.quiz_result, name='quiz_result'),
]
