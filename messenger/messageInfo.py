from django import forms
from .models import Message

class messageInfo(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'draft', 'text']
