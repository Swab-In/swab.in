from django import forms
# from django.contrib.auth.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser

# class UserRegistrationForm(forms.ModelForm):
#     # name = forms.CharField(max_length=100, required=True)
#     # username = forms.CharField(max_length=100, required=True)
#     # email = forms.EmailField(max_length=100, required=True)
#     # pekerjaan = forms.CharField(max_length=50, required=True)
#     # umur = forms.CharField(max_length=30, required=True)
#     # tanggal_lahir = forms.DateField(required=True)
#     # password = forms.CharField(max_length=20, required=True, widget= forms.PasswordInput)
#     # re_password = forms.CharField(max_length=20, required=True)
#     class Meta:
#         model = UserProfile
#         # model = User
#         fields = "__all__"


class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "username", "email",
                  "pekerjaan", "umur", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class UserLoginForm(forms.ModelForm):
#     class Meta:
#         # model = User
#         model = UserProfile
#         fields = "username", "password"
#         widgets = {
#             'username' : forms.widgets.TextInput(attrs={'placeholder':'username anda'}),
#             'password' : forms.widgets.TextInput(attrs={'placeholder':'masukkan password'}),
#         }

#         help_texts = {
#             'username': None,
#         }

#         labels = {'username' : 'Username', 'password' : 'Password'}
