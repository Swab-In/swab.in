from .models import Komentar
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['komen']