from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        user = User.objects.filter(email=self.cleaned_data.get('email'))
        if user:
            raise forms.ValidationError('This email already exists please choose a different one.')
        return super(UserRegisterForm, self).clean()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        # user = User.objects.filter(email=self.cleaned_data.get('email'))
        # if user:
        #     raise forms.ValidationError('This email already exists please choose a different one.')
        return super(UserUpdateForm, self).clean()


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['nickname', 'image', 'intro', 'url']