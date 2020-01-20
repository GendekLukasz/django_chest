from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chest-home'),
    path('game', views.game, name='chest-game'),
    path('start', views.start_game, name='chest-start'),
    path('move', views.move, name='chest-move'),
]
