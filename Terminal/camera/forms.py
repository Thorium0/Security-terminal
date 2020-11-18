from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Camera

class CameraAddForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['title', 'ip']
        labels = {
            'title': _('Titel'),
            'ip': _('Adresse')
        }
