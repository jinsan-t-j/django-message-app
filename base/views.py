from email.mime import message
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from .models import Room
from .forms import RoomForm

# Create your views here.

# def showLoginForm(request):
#     return render(request, 'auth/login.html')

def loginAction(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base:home')
        else: 
            messages.error(request, 'Invalid user credentials')
    return render(request, 'auth/login.html')

def registerAction(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('base:home')
        else:
            messages.error(request, 'An error occurred')
    compact = {
        'form': UserCreationForm()
    }
    return render(request, 'auth/register.html', compact)

def home(request):
    rooms = Room.objects.all()
    compact = {
        'rooms': rooms
    }
    return render(request, 'home/index.html' , compact)

def room(request, id):
    room = Room.objects.get(id=id);
    compact = {
        'room': room
    }
    return render(request, 'rooms/show.html' , compact)

def createRoom(request):
    compact = {
        'form': RoomForm
    }
    return render(request, 'rooms/create.html', compact)

def storeRoom(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')

def editRoom(request, id):
    room = Room.objects.get(id=id)
    compact = {
        'room': room,
        'form': RoomForm(instance=room)
    }
    return render(request, 'rooms/edit.html', compact)

def updateRoom(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('base:home')


def destroyRoom(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        room.delete()
        return redirect('base:home')
    compact = {
        'obj': room.name
    }
    return render(request, 'defaults/delete.html', compact)

