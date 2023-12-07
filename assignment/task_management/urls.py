
from django.contrib import admin
from django.urls import path,include
from task_management.views import home


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path("task/", include('task.urls')),
    path("category/", include('category.urls')),
]
