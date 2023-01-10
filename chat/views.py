from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse

from chat.forms import RoomForm
from chat.models import Room


def index(request: HttpRequest) -> HttpResponse:
    room_queryset = Room.objects.all()

    return render(request, "chat/index.html", {
        "room_list": room_queryset
    })


@login_required
def room_chat(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    return render(request, "chat/room_chat.html", {
        "room": room
    })


@login_required
def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            created_room = form.save()
            return redirect("chat:room_chat", created_room.pk)
    else:
        form = RoomForm()

    return render(request, "chat/room_form.html", {
        "form": form,
    })

# class RoomCreateView(LoginRequiredMixin, CreateView):
#     form_class = RoomForm
#     template_name = "chat/room_form.html"
#
#     def get_success_url(self):
#         created_room = self.object
#         return resolve_url("chat:room_chat", created_room.pk)
#
#
# room_new = RoomCreateView.as_view()
