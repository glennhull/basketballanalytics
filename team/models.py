# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
	team_id = models.CharField(max_length=200)
	team_slug = models.CharField(max_length=200)
	ppg = models.DecimalField(max_digits=5, decimal_places=1)
	apg = models.DecimalField(max_digits=5, decimal_places=1)
	rpg = models.DecimalField(max_digits=5, decimal_places=1)
	bpg = models.DecimalField(max_digits=5, decimal_places=1)
	spg = models.DecimalField(max_digits=5, decimal_places=1)	
	fga = models.DecimalField(max_digits=5, decimal_places=1)
	fgm = models.DecimalField(max_digits=5, decimal_places=1)
	tpg = models.DecimalField(max_digits=5, decimal_places=1)
	threept_attempted = models.DecimalField(max_digits=5, decimal_places=1)
	threept_made = models.DecimalField(max_digits=5, decimal_places=1)
	fastbreak_points = models.DecimalField(max_digits=5, decimal_places=1)
	paint_points = models.DecimalField(max_digits=5, decimal_places=1)
	turnover_points = models.DecimalField(max_digits=5, decimal_places=1)
	secondchance_points = models.DecimalField(max_digits=5, decimal_places=1)