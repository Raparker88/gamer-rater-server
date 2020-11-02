"""Image model module"""
from django.db import models


class Image(models.Model):
    """Image database model"""
    playergame = models.ForeignKey("PlayerGame", on_delete=models.CASCADE)
    image = models.ImageField()
