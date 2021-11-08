from datetime import datetime
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=50, default='')
    note = models.CharField(max_length=100)

    def __str__(self):
        return self.note


class Toy(models.Model):
    name = models.CharField(max_length=100)
    games = models.ManyToManyField(Game, verbose_name="list of games")
    VAR_STATUS = [
        ('o', 'ok'),
        ('b', 'broken'),
        ('r', 'repair')
    ]
    status = models.CharField(max_length=50, choices=VAR_STATUS, default='o')
    status_update = models.DateTimeField(default=datetime.now, null=False, blank=False)

    def __str__(self):
        return self.name


