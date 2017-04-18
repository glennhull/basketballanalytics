# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from player.models import Player
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from stattlepy import Stattleship

def player_page(request, player_name): 
	New_query = Stattleship()
	Token = New_query.set_token('46a96fa056bca68ddb8835f70ad68974')
	player_id = "nba-%s" % player_name
	season_stats = New_query.ss_get_results(sport='basketball',league='nba', ep='player_season_stats', player_id=player_id)
	player_bio = New_query.ss_get_results(sport='basketball',league='nba', ep='player')
	ppg = season_stats[0]['player_season_stats'][0]['average_points']
	apg = season_stats[0]['player_season_stats'][0]['average_assists']
	rpg = season_stats[0]['player_season_stats'][0]['average_rebounds']
	template = loader.get_template('player/index.html')
	context = {
		'player_name' : player_name,
		'output': season_stats,
		'ppg' : ppg,
		'apg' : apg,
		'rpg' : rpg,
	}
	player_entry_count = Player.objects.filter(player_name = player_name).count()
	if player_entry_count == 0:
		add_player(player_name)

	return HttpResponse(template.render(context, request))

def add_player(player_name):
	print "adding player"
	pl = Player.objects.create(player_name = player_name);	
	pl.save()

