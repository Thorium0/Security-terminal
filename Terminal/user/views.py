from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login as DjangoLogin
from django.contrib.auth import logout as DjangoLogout
from django.contrib.auth.decorators import login_required
from picamera import PiCamera
from time import sleep
import face_recognition
import os

@login_required
def logout(request):
    DjangoLogout(request)
    return redirect("login")

encodings = []

def doLogin():
            camera = PiCamera()
            mediaUrl = os.path.join(os.path.dirname(__file__), "static", "user")
            names = ["Troels", "Anders", "Alexander"]
            if len(encodings) < 1:
                faces = [name.lower()+".jpg" for name in names]
                for face in faces:
                    img1 = face_recognition.load_image_file(os.path.join(mediaUrl, face))
                    encodings.append(face_recognition.face_encodings(img1)[0])


            camera.resolution = (160, 120)
            camera.capture(os.path.join(mediaUrl, "cap.jpg"))
            camera.close()
            img2 = face_recognition.load_image_file(os.path.join(mediaUrl, "cap.jpg"))
            encoding2 = face_recognition.face_encodings(img2)
            if len(encoding2) < 1:
                return False
            else:
                encoding2 = encoding2[0]

            for x in range(len(encodings)):
                results = face_recognition.compare_faces([encodings[x]], encoding2)
                if results[0] == True:
                    username = names[x]
                    return username
                else:
                    return False


def login(request):
    username = doLogin()
    if username:
        user = User.objects.get(username=username)
        DjangoLogin(request, user)
        return redirect("home")

    else:
        context = {
        'title': "Login",
        }
        return render(request, 'user/login.html.django', context)
