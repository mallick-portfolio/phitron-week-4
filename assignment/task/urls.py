

from django.urls import path
from task.views import create_task, edit_task, delete_task
urlpatterns = [
    path('create-task/', create_task, name="create_task"),
    path('edit-task/<int:task_id>', edit_task, name="edit_task"),
    path('delete-task/<int:task_id>', delete_task, name="delete_task"),
]
