
from django.contrib import admin
from django.urls import path,include
from folkMusician.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='home'),
    path('musician/', include("musician.urls")),
    path('album/', include("album.urls")),
]
