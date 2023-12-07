from django.db import models
from musician.models import Musician
import datetime
# Create your models here.
# Album Name
# One-to-Many Relationships with musician model
# Album release date
# Rating between 1-5


class Album(models.Model):
  RATING = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
  )
  name = models.CharField(max_length=200)
  musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
  release_date = models.DateTimeField(auto_now=True)
  rating = models.CharField(choices=RATING, max_length=20, null=True, blank=True)

  def __str__(self):
      return self.name
  