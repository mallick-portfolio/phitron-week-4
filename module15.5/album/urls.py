
from django.urls import path
from album.views import create_album,edit_album
urlpatterns = [
    path('create/', create_album, name="create_album"),
    path('edit/<int:id>', edit_album, name="edit_album"),
]
