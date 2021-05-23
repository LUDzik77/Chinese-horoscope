from django import forms
from .models import Postentry

class PostentryModelForm(forms.ModelForm):
    class Meta:
        model = Postentry
        fields = ['author', 'description']