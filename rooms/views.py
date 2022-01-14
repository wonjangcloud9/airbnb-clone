from django.shortcuts import render
from datetime import date, datetime
from . import models


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
        },
    )
