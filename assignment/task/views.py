from django.shortcuts import render
from task.forms import TaskForm
# Create your views here.


def create_task(request):
  form = TaskForm()
  return render(request, './task/form.html', {"form": form})