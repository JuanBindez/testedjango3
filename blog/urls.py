from django.contrib import admin
from django.urls import path
from .views import hello_world
from .views import teste

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('teste/', teste),
]
