from django.shortcuts import render, get_object_or_404
from meetings.models import *


def rooms(request):
    return render(request, 'rooms/summary.html', {
        'rooms': Room.objects.all()
    })


def details(request, id):
    return render(request, 'rooms/details.html', {
        'room': get_object_or_404(Room, pk=id)
    })
