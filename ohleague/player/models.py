from __future__ import unicode_literals

from django.db import models
from team.models import Team

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    gp = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    a = models.IntegerField(default=0)
    jersey_number = models.IntegerField(default=-1)