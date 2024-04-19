from django.shortcuts import render, redirect, get_object_or_404
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
        form = FichierForm(request.POST or None)
        if form.is_valid():
            form.save()
        redirect('create')
    
    form = FichierForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)



def editFile(request, id):

    file = get_object_or_404(Fichier, id=id)

    form = FichierForm(request.POST or None, instance=file)
    if form.is_valid():
        form.save()

        form = FichierForm()
    
        redirect('/')
    
    # form = FichierForm()

    context = {
        # 'file': file,
        'form': form
    }
    return render(request, 'edit.html', context)



def deleteFile(request, id):

    file = get_object_or_404(Fichier, id=id)

    name = file.nom
    if request.method == 'POST':
        
        file.delete()
        
        redirect('/home')

    context = {
        'nom': name
    }

    return render(request, 'delete.html',context)
     
     