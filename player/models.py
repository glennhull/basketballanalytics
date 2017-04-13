# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Player(models.Model): 
	player_name = models.CharField(max_length=200)

class Season_Stats(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	ppg = models.DecimalField(max_digits=5, decimal_places=1)
	apg = models.DecimalField(max_digits=5, decimal_places=1)
	rpg = models.DecimalField(max_digits=5, decimal_places=1)
	per = models.DecimalField(max_digits=5, decimal_places=2)
