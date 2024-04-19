from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from .models import * 
from .form import *

from django.contrib.auth import login, logout, authenticate, hashers
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def displayFiles(request):

    data = Fichier.objects.all().values()

    context = {
       'files': data    
    }
    print(context) 
     
    return render(request, 'home.html', context)

@login_required
def createFiles(request):

    if request.method == 'POST':
        form = FichierForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/create')
    
    form = FichierForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


@login_required
def editFile(request, id):

    file = get_object_or_404(Fichier, id=id)

    form = FichierForm(request.POST or None, instance=file)
    if form.is_valid():
        form.save()

        form = FichierForm()
    
        return redirect('/')
    
    # form = FichierForm()

    context = {
        # 'file': file,
        'form': form
    }
    return render(request, 'edit.html', context)


@login_required
def deleteFile(request, id):

    file = get_object_or_404(Fichier, id=id)

    name = file.nom
    if request.method == 'POST':
        
        file.delete()
        
        return redirect('/')

    context = {
        'nom': name
    }

    return render(request, 'delete.html',context)


def register(request):

    if request.method == 'POST':
        
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            message = messages.success(request, "Inscription réussie")
            return redirect('/login')
        else:
            message = messages.error(request, "Erreur lors de l'inscription")
            print('echec')


    return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = hashers.make_password(request.POST['password'])

        print(email, password)
        user = authenticate(request, email=email, password=password)
        # user = get_object_or_404(User, email=email, password=password)

        print(user)
        if user is not None and user.is_active:
            login(request, user)
            
            message = messages.success(request, "Connexion réussie")
            
            return redirect('/')
            
        else:
            message = messages.error(request, "Erreur d'authentification")

            print('echec')
            return redirect('/login')

    return render(request, 'login.html')


@login_required
def logout(request):
    logout(request)
     
     