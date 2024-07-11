from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Option, Result, Area
from .forms import QuestionForm

def take_quiz(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        form = QuestionForm(request.POST, questions=questions)
        if form.is_valid():
            scores = {area.id: 0 for area in Area.objects.all()}
            for question in questions:
                option_id = form.cleaned_data[f'question_{question.id}']
                option = Option.objects.get(id=option_id)
                scores[option.area.id] += 1

            max_area_id = max(scores, key=scores.get)
            max_area = Area.objects.get(id=max_area_id)

            result = Result(
                student_name=request.POST['student_name'],
                student_email=request.POST['student_email'],
                area=max_area,
                score=scores[max_area_id]
            )
            result.save()
            return redirect('quiz_result', result_id=result.id)
    else:
        questions = Question.objects.all()
        form = QuestionForm(questions=questions)
    return render(request, 'quiz/take_quiz.html', {'form': form})

def quiz_result(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    return render(request, 'quiz_result.html', {'result': result})
