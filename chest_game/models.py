from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GameModel(models.Model):
    name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    white_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='white_player_games')
    black_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='black_player_games')
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='win_games')