"""Image model module"""
from django.db import models


class Image(models.Model):
    """Image database model"""
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="image")
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="image")
    image = models.ImageField()
