from __future__ import unicode_literals

from django.db import models

# Create your models here.
class League(models.Model):
    league_name = models.CharField(max_length=1)