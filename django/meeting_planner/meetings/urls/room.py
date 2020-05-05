from django.urls import path
from meetings.views.rooms import rooms, details

urlpatterns = [
    path('', rooms, name='room_list'),
    path('<int:id>', details, name='room_details'),
]
