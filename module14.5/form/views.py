from django.shortcuts import render
from form.forms import ContactForm, GreekForm, StudentForm
# Create your views here.
def home(request):
  form = ContactForm()
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      print("form", form.cleaned_data)
      return render(request,'./form/contactform.html', {"form": form})
  return render(request,'./form/contactform.html', {"form": form})


def form2(request):
  form = GreekForm()
  if request.method == "POST":
    form = GreekForm(request.POST)
    if form.is_valid():
      print("form", form.cleaned_data)
      return render(request,'./form/form2.html', {"form": form})
  return render(request,'./form/form2.html', {"form": form})


  
def student_form(request):
  form = StudentForm()
  if request.method == "POST":
    form = StudentForm(request.POST)
    if form.is_valid():

      print("form", form.cleaned_data)
      return render(request,'./form/form2.html', {"form": form})
  return render(request,'./form/form2.html', {"form": form})
