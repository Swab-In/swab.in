from django import forms
from django.forms.widgets import Textarea
from swab_vaksin.models import SwabInformation, VaksinInformation, Experience

class PengalamanForm(forms.ModelForm):
    class Meta:
        model = Experience
        # fields = (
        #     'pengalaman',
        # )
            

        fields = "__all__"
        # widget = {
        #     'pengalaman' : Textarea
        # }

        # pengalaman = forms.CharField(label='', required=True, max_length=300, widget=forms.Textarea)