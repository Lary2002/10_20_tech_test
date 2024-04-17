from django.contrib import admin
from .models import *

# Register your models here.

class FichierAdmin(admin.ModelAdmin):
    list_display = ['nom', 'taille', 'date_upload']

admin.site.register(Fichier, FichierAdmin)

