from django.db import models

# Create your models here.

class Fichier(models.Model):
    nom = models.CharField(max_length=255)
    taille = models.PositiveIntegerField()
    date_upload = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
    

