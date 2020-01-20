from django.urls import path, include
from django.contrib import admin
from chest_game import views

urlpatterns = [
    path('play/', include('chest_game.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('main/', views.main, name='chest-main'),
    path('', views.main, name='chest-main')
]
