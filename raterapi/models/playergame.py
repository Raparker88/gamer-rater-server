"""PlayerGame model module"""
from django.db import models


class PlayerGame(models.Model):
    """PlayerGame database model"""
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="currently_playing")
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="currently_playing")
    review = models.CharField(max_length=500)
    rating = models.IntegerField()