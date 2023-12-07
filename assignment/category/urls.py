
from django.urls import path
from category.views import create_category

urlpatterns = [
    path('create-category/',create_category, name="create_category"),
]
