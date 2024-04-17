
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', displayFiles, name='home'),
    path('create/', createFiles, name='create'),
]