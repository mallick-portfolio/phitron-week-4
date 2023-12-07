from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import Musician



# Create your views here.
def create_musician(request):
  print(request.method)
  form = MusicianForm()
  if request.method == "POST":
    form = MusicianForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
    return redirect('home')
  else:
    return render(request, './musician/createForm.html', {"form": form, "title":"Create Musician"})



# def edit_musician(request, id):
#   print("id", id)
#   musician = Musician.objects.filter(id=id).first()
#   form = MusicianForm(instance=musician)
#   if request.method == "POST":
#     form = MusicianForm(request.POST)
#     if form.is_valid():
#       form.save()
#     return redirect('home')
#   else:
#     return render(request, './musician/createForm.html', {"form": form})

def edit_musician(request, id):
  musician = Musician.objects.get(pk=id)
  print(musician)
  form = MusicianForm(instance=musician)
  if request.method == "POST":
    form = MusicianForm(request.POST, instance=musician)
    if form.is_valid():
      form.save()
    return redirect('home')
  return render(request, './musician/createForm.html', {"form": form})