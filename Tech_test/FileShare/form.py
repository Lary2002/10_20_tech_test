from .models import *
from django.forms import ModelForm

class FichierForm(ModelForm):

    class Meta:
        model = Fichier
        fields = ['nom', 'taille',]