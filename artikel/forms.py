from .models import Komentar
from django import forms

class NoteForm(forms.ModelForm):
    class Meta:
        
        model = Komentar
        fields = "__all__"