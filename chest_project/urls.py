from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('play/', include('chest_game.urls')),
    path('admin/', admin.site.urls),
]
