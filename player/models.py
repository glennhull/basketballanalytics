# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Player(models.Model):
	player_id = models.CharField(max_length=200)
	player_name = models.CharField(max_length=200)
	position = models.CharField(max_length=10)
	team_id = models.CharField(max_length=200)
		
class Season_Stats(models.Model):
	player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
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
	
class Game_Logs(models.Model): 
	game_log_id = models.CharField(max_length=200)
	player_id = models.CharField(max_length=200)
	team_id = models.CharField(max_length=200)
	opponent_id = models.CharField(max_length=200)
	home_team_score = models.DecimalField(max_digits=5, decimal_places=1)
	away_team_score = models.DecimalField(max_digits=5, decimal_places=1)
	team_score = models.DecimalField(max_digits=5, decimal_places=1)
	team_outcome = models.CharField(max_length=200)
	ppg = models.DecimalField(max_digits=5, decimal_places=1)
	apg = models.DecimalField(max_digits=5, decimal_places=1)
	rpg = models.DecimalField(max_digits=5, decimal_places=1)
	bpg = models.DecimalField(max_digits=5, decimal_places=1)
	spg = models.DecimalField(max_digits=5, decimal_places=1)	
	fga = models.DecimalField(max_digits=5, decimal_places=1)
	fgm = models.DecimalField(max_digits=5, decimal_places=1)
	tpg = models.DecimalField(max_digits=5, decimal_places=1)