from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='chest-play'),
    path('admin/', admin.site.urls),
]
