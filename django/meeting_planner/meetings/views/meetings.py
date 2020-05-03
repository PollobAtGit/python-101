from django.shortcuts import render, get_object_or_404
from meetings.models import Meetings


def meetings(request):
    return render(request, 'meetings/summary.html', {
        'meetings': Meetings.objects.all()
    })


def details(request, id):
    return render(request, 'meetings/details.html', {
        'current_meeting': get_object_or_404(Meetings, pk=id)
    })
