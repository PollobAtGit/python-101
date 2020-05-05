from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from meetings.models import Meetings


def meetings(request):
    return render(request, 'meetings/summary.html', {
        'meetings': Meetings.objects.all()
    })


def details(request, id):
    return render(request, 'meetings/details.html', {
        'current_meeting': get_object_or_404(Meetings, pk=id)
    })


MeetingForm = modelform_factory(Meetings, exclude=[])


def create_meeting(request):
    if request.method == 'POST':
        meeting_form = MeetingForm(request.POST)
        if meeting_form.is_valid():
            meeting_form.save()
            return redirect("/meeting")

    return render(request, 'meetings/create.html', {
        'form': MeetingForm()
    })
