from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cameras'),
    path('add/', views.addCam, name='addCam'),
    path('remove/<id>', views.removeCam, name='removeCam')
]
