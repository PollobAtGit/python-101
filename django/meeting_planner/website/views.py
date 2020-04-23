from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse('welcome to meeting planner')


def now(request):
    return HttpResponse(f'current time {str(datetime.now().ctime())}')


def about(request):
    name = request.GET.get('name', '')
    return HttpResponse(f'i am {name}')


# add model app but for now

class Meeting:
    pass


