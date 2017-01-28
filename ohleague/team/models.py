from __future__ import unicode_literals

from django.db import models
from league.models import League

# Create your models here.
class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name