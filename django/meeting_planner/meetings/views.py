from django.shortcuts import render, get_object_or_404
from .models import *


def details(request, id):
    return render(request, 'meetings/details.html', {
        'current_meeting': get_object_or_404(Meetings, pk=id)
    })


def rooms(request):
    return render(request, 'rooms/summary.html', {
        'rooms': Room.objects.all()
    })


def room_details(request, id):
    return render(request, 'rooms/details.html', {
        'room': get_object_or_404(Room, pk=id)
    })
