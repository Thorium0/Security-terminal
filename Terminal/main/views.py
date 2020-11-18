from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    username = ""
    if request.user.is_authenticated:
        username = request.user.username
    context = {
    "username" : username,
    "title" : "Home"
    }
    return render(request, 'main/home.html.django', context)
