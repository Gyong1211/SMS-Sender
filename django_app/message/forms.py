from django import forms
from django.forms import Textarea

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'recipient',
            'content',
        ]
        widgets = {
            'content': Textarea(),
        }
