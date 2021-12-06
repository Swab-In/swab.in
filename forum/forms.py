from django import forms
from .models import *

class ForumForm(forms.ModelForm):
	class Meta:
		model = Forum
		fields = ['title','message','image']

class KomentarForm(forms.ModelForm):
	class Meta:
		model = Komentar
		fields = ['komentar']