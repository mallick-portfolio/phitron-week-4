

from django.urls import path
from task.views import create_task
urlpatterns = [
    path('create-task/', create_task, name="create_task"),
]
