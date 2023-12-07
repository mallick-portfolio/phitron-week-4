from django import forms
from django.forms.widgets import NumberInput
import datetime
from form.models import Student



class ContactForm(forms.Form):
# choice option
  BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
  FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


  name = forms.CharField(max_length=20)
  email = forms.EmailField(required=False,label="Please enter your email address",initial="example@gmail.com")
  comments = forms.CharField(widget=forms.Textarea(attrs=({"rows": 2, "columns": 2})))
  date = forms.DateField(initial=datetime.date.today,widget=NumberInput(attrs=({"type": "date" })), )
  agree = forms.BooleanField(initial=True)
  birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
  value = forms.DecimalField()
  favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)



class GreekForm(forms.Form):
  title = forms.CharField() 
  description = forms.CharField()
  first_name = forms.CharField(max_length = 200)  
  last_name = forms.CharField(max_length = 200)  
  roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")  
  password = forms.CharField(widget = forms.PasswordInput())


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = "__all__"
    widgets = {
      "date_field": forms.DateInput(attrs={"type": 'date'})
    }