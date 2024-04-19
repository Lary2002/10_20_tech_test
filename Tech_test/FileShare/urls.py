
from django.urls import path
from .views import *

urlpatterns = [
    path('', displayFiles, name='home'),
    path('create/', createFiles, name='create'),
    path('edit/<int:id>', editFile, name='edit'),
    path('delete/<int:id>', deleteFile, name='delete'),
]