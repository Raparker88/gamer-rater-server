"""Review model module"""
from django.db import models


class Review(models.Model):
    """Review database model"""
    playergame = models.ForeignKey("PlayerGame", on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)