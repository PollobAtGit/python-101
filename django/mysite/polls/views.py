from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return HttpResponse("<br>".join([question.question_text for question in latest_question_list]))

def details(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def results(request, question_id):
    return HttpResponse('You are looking at the results of question %s' % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s' % question_id)
