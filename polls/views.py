from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by('-pud_date')[:5]
    context = {'lastest question list': latest_question_list, }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You're looking at results of " + question_id)


def vote(request, question_id):
    return HttpResponse("You're voting for question " + question_id)
