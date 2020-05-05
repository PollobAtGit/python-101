from django.urls import path
from meetings.views.meetings import meetings, details

urlpatterns = [
    path('', meetings, name='meeting_list'),
    path('<int:id>', details, name='meeting_details'),
]
