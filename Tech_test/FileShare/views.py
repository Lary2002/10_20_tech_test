from django.shortcuts import render, redirect
from django.http import request
from .models import * 
from .form import *

# Create your views here.

def displayFiles(request):

    data = Fichier.objects.all().values()

    context = {
       'files': data   
    }
    print(context)
     
    return render(request, 'home.html', context)


def createFiles(request):

    if request.method == 'POST':
        form = FichierForm(request.POST).save()
        # message = 'Le Fichier a bien été créé'
        redirect('create')
    else:
        # message = 'Le Fichier n\'a pas été créé'
        form = FichierForm()

    context = {
        'form': form,
        # 'message': message
    }
    
    return render(request, 'create.html', context)
     
     