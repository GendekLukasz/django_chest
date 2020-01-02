from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chest-play'),
    path('main', views.main, name='chest-main')
]
