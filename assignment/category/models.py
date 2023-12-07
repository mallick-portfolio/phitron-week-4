from django.db import models
from task.models import Task
# Create your models here.
class Category(models.Model):
  # Category Name
  # Many-to-Many Relationships with task model  
  name = models.CharField(max_length=50)
  task = models.ManyToManyField(Task)

  def __str__(self):
      return self.name
  