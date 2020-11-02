from django.db import models


class Game(models.Model):
    number_of_players = models.IntegerField()
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=75)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    time_to_play = models.CharField(max_length=50)
    age_recommendation = models.CharField(max_length=50)