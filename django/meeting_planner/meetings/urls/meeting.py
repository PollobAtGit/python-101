from django.urls import path
from meetings.views.meetings import meetings, details, create_meeting

urlpatterns = [
    path('', meetings, name='meeting_list'),
    path('create', create_meeting, name='create_meeting'),
    path('<int:id>', details, name='meeting_details'),
]
