from django.db import models
from django.core import validators
import datetime
# Create your models here.


class Student(models.Model):
  auto_field = models.AutoField(primary_key=True)
  # big_auto_field = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=20)
  email_field = models.EmailField()
  big_integer_field = models.BigIntegerField()
  binary_field = models.BinaryField()
  boolean_field = models.BooleanField()
  char_field = models.CharField(max_length=255)
  # comma_separated_field = models.CharField(
  #       validators=[validators.comma_separated_validator],
  #       max_length=255
  #   )
  date_field = models.DateField(default=datetime.date.today)
  decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
  duration_field = models.DurationField()
  file_field = models.FileField(upload_to='files/', blank=True, null=True)


