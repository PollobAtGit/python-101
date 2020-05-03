from datetime import time
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    floor = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


# return f'Room {self.number} at floor {self.floor}'


class Meetings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
