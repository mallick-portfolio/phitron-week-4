
from django.urls import path
from musician.views import create_musician, edit_musician
urlpatterns = [
    path('create/', create_musician, name='create_musician'),
    path('edit/<int:id>', edit_musician, name='edit_musician'),
]
