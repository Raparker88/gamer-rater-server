"""PlayerGame model module"""
from django.db import models


class Rating(models.Model):
    """PlayerGame database model"""
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="rating")
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="rating")
    rating = models.IntegerField()