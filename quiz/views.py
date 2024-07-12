from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Option, Result, Area
from .forms import QuestionForm, StudentInfoForm

def take_quiz(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        question_form = QuestionForm(request.POST, questions=questions)
        student_form = StudentInfoForm(request.POST)
        if question_form.is_valid() and student_form.is_valid():
            scores = {area.id: 0 for area in Area.objects.all()}
            total_questions = questions.count()

            for question in questions:
                option_id = question_form.cleaned_data.get(f'question_{question.id}')
                if option_id:
                    option = Option.objects.get(id=option_id)
                    scores[option.area.id] += 1

            max_area_id = max(scores, key=scores.get)
            max_area = Area.objects.get(id=max_area_id)

            # Calcula a pontuação em porcentagem
            score_percentage = (scores[max_area_id] / total_questions) * 100

            result = Result(
                student_name=student_form.cleaned_data['student_name'],
                student_email=student_form.cleaned_data['student_email'],
                whatsapp=student_form.cleaned_data['whatsapp'],
                school_name=student_form.cleaned_data['school_name'],
                area=max_area,
                score=score_percentage
            )
            result.save()
            return redirect('quiz_result', result_id=result.id)
    else:
        questions = Question.objects.all()
        question_form = QuestionForm(questions=questions)
        student_form = StudentInfoForm()
    return render(request, 'quiz/take_quiz.html', {'question_form': question_form, 'student_form': student_form})

def quiz_result(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    return render(request, 'quiz/quiz_result.html', {'result': result})
