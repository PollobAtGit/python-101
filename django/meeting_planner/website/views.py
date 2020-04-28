
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    content = {
            'message' : 'welcome message from plurasight course',
            'content_url' : 'https://app.pluralsight.com/course-player?clipId=a46b1c63-ed7d-427b-882f-cccdf6e65a11',
            'date'    : datetime.now()
            }

    return render(request, 'website/welcome.html', content)
    #return HttpResponse('welcome to meeting planner')


def now(request):
    return HttpResponse(f'current time {str(datetime.now().ctime())}')


def about(request):
    name = request.GET.get('name', '')
    return HttpResponse(f'i am {name}')

