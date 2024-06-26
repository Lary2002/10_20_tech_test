from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):

    class Meta: 
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class FichierForm(ModelForm):

    class Meta:
        model = Fichier
        fields = ['nom', 'taille',]