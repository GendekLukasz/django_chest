from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('play/', include('chest_game.urls')),
]
