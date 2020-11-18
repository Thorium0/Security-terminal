from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Camera

class CameraAddForm(forms.ModelForm):
    ip = forms.GenericIPAddressField()
    class Meta:
        model = Camera
        fields = ['title', 'ip']
        labels = {
            'title': _('Titel')
        }
