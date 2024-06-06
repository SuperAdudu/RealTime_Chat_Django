from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request,room):
    username = request.GET['username']
    room_details = Room.objects.get(name=room)
    return render(request,'room.html',{'username':username,'room':room,'room_details':room_details})

def checkview(request):
    room = request.POST['room_name']
    userName = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+userName)
    else:
        newRoom = Room.objects.create(name=room)
        newRoom.save()
        return redirect('/'+room+'/?username='+userName) 

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message,nameUser=username,room=room_id)
    new_message.save()
    return HttpResponse('Message sent success')

def getMessages(request,room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})