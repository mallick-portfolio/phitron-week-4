from django.shortcuts import render, redirect
from album.forms import AlbumForm
from album.models import Album


# Create your views here.
def create_album(request):
  form = AlbumForm()
  if request.method == "POST":
    form = AlbumForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('home')
  return render(request, './album/createForm.html', {"form": form})

  
def edit_album(request, id):
  album = Album.objects.filter(id=id).first()
  form = AlbumForm(instance=album)
  if request.method == "POST":
    form = AlbumForm(request.POST, instance=album)
    
    if form.is_valid():
      form.save()
    return redirect('home')
  return render(request, './album/createForm.html', {"form": form})