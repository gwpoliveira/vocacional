from django import forms
from .models import Question, Option

class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            options = Option.objects.filter(question=question)
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.text,
                choices=[(option.id, option.text) for option in options],
                widget=forms.RadioSelect
            )

class StudentInfoForm(forms.Form):
    student_name = forms.CharField(
        label='Nome',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    student_email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    whatsapp = forms.CharField(
        label='Whatsapp',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    school_name = forms.CharField(
        label='Nome da Escola',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
