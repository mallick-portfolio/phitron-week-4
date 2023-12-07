from django.db import models

# Create your models here.
class Task(models.Model):
#   taskTitle 
# taskDescription 
# is_completed by default False
# Task Assign Date
  title = models.CharField(max_length=200)
  description = models.TextField()
  is_completed = models.BooleanField(default=False)
  assign_at = models.DateTimeField(auto_now_add=True)


  def __str__(self):
      return self.title
  