
from django.urls import path
from .views import *

urlpatterns = [
    path('', displayFiles, name='home'),
    path('create/', createFiles, name='create'),
]