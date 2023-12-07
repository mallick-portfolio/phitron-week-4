
from django.urls import path, include
from form.views import home, form2, student_form
urlpatterns = [
    path('', home, name='home'),
    path('form2/', form2, name='form2'),
    path('student-form/', student_form, name='student_form'),
]
