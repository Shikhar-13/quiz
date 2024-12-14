from django.shortcuts import render , redirect
import requests
from .models import Question , Choice

# Create your views here.
def fetch_data(request):
    """Using api url to get the questions from database"""
    Question.objects.all().delete()
    url = 'https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple'
    response = requests.get(url)
    data = response.json()
    for i in data.get('results',[]):
        question = Question.objects.create(question_text=i['question'])
        choices = Choice.objects.create(question=question,choice_text=i['correct_answer'],is_correct=True)
        for j in i['incorrect_answers']:
            Choice.objects.create(question=question,choice_text=j,is_correct=False)
    return redirect('quiz')

def index(request):
    question = Question.objects.all()
    context = {'question':question}
    return render(request, 'quiz/index.html',context)

def quiz(request):
    if not Question.objects.exists():
        return redirect('fetch_data')

    if request.method == 'POST':
        score = 0
        total_questions = Question.objects.count()
        
        detailed_results = []
        
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(f'question_{question.id}')
            
            selected_choice = None
            correct_choice = question.choices.filter(is_correct=True).first()
            
            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                
                if selected_choice.is_correct:
                    score += 1
                    result = 'correct'
                else:
                    result = 'incorrect'
            else:
                result = 'not_answered'
            
            detailed_results.append({
                'question': question.question_text,
                'selected_choice': selected_choice.choice_text if selected_choice else None,
                'correct_choice': correct_choice.choice_text,
                'result': result
            })
        
        context = {
            'score': score,
            'total_questions': total_questions,
            'percentage': (score / total_questions) * 100 if total_questions > 0 else 0,
            'detailed_results': detailed_results,
            'correct_count': score,
            'incorrect_count': total_questions - score,
            'not_answered_count': 0 
        }
        return render(request, 'quiz/index.html', context)
    
    questions = Question.objects.prefetch_related('choices').all()
    context = {'questions': questions}
    return render(request, 'quiz/quiz.html', context)
