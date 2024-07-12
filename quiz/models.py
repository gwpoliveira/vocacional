# quiz/models.py
from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Result(models.Model):
    student_name = models.CharField(max_length=255)
    student_email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    school_name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.student_name} - {self.area.name} ({self.score})'
