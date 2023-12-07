from django.shortcuts import render,redirect
from task.forms import TaskForm
from task.models import Task
# Create your views here.


def create_task(request):
  form = TaskForm()
  if request.method == "POST":
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return redirect('home')
  return render(request, './task/form.html', {"form": form})

def edit_task(request, task_id):
  task = Task.objects.filter(id=task_id).first()
  form = TaskForm(instance=task)
  if request.method == "POST":
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save(commit=True)
      return redirect('home')
  return render(request, './task/form.html', {"form": form})

def delete_task(request, task_id):
  task = Task.objects.filter(id=task_id).first()
  task.delete()
  return redirect('home')
