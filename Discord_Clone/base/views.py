from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name':'pyton'},
    {'id': 2, 'name':'Django'},
    {'id': 3, 'name':'JavaScript'},
    {'id': 4, 'name':'React'},
]

def home(request):
    # return HttpResponse("Home Page")
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    # return HttpResponse("Room Page")
    return render(request, 'base/room.html', context)