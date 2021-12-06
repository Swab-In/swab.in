from django import forms
# from django.contrib.auth.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "username", "email",
                  "pekerjaan", "umur", "userpic", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
