from django.shortcuts import render
from .models import Room
from .forms import RoomForm
from django.http import HttpResponse
# Create your views here.

# rooms = [
#     {'id': 1, 'name':'python'},
#     {'id': 2, 'name':'Django'},
#     {'id': 3, 'name':'JavaScript'},
#     {'id': 4, 'name':'React'},
# ]

def home(request):
    # return HttpResponse("Home Page")
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room':room}
    # return HttpResponse("Room Page")
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)