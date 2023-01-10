from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html")


def room_chat(request, room_name):
    return render(request, "chat/room_chat.html", {
        "room_name": room_name,
    })
