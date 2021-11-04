from django import forms
from swab_vaksin.models import *

class PengalamanSwabForm(forms.ModelForm):
    class Meta:
        model = SwabExperience
        fields = ['pengalamanSwab']

class PengalamanVaksinForm(forms.ModelForm):
    class Meta:
        model = VaksinExperience
        fields = ['pengalamanVaksin']