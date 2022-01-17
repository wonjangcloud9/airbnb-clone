from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator, EmptyPage


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(
            request,
            "rooms/home.html",
            context={
                "page": rooms,
            },
        )
    except EmptyPage:
        return redirect("/")
