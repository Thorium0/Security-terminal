from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CameraAddForm
import os


@login_required
def home(request):
    username = ""
    if request.user.is_authenticated:
        username = request.user.username
    context = {
    "username" : username,
    "title" : "Cameras"
    }
    return render(request, 'camera/cameras.html.django', context)



@login_required()
def addCam(request):
    username = ""
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        form = CameraAddForm(request.POST)
        if form.is_valid():
            try: form.save()
            except: messages.error(request, "Error")
            else:
                messages.success(request, "Camera tilføjet!")
                #pid = os.system("pidof matchbox-keyboard")
                #os.system("kill "+str(pid))
        return redirect('cameras')

    else:
        form = CameraAddForm()
        os.system("DISPLAY=:0 matchbox-keyboard &")
    context = {
    "username" : username,
    "title" : "Add Camera",
    "form" : form
    }
    return render(request, 'camera/addCam.html.django', context)
