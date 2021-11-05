from django import forms
from django.db.models import fields
from about.models import Pesan

class ContactForm(forms.ModelForm):
    class Meta:
        model = Pesan
        fields = "__all__"