from django import forms
from .models import Forum

class ForumForm(forms.ModelForm):
	class Meta:
		model = Forum
		fields = "__all__"
		labels = {
            'title': 'Judul',
			'message' : 'Diskusi',
			'image' : 'Thumbnail',
        }