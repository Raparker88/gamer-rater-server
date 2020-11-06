"""Review model module"""
from django.db import models


class Review(models.Model):
    """Review database model"""
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="review")
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="review")
    review = models.CharField(max_length=1000)