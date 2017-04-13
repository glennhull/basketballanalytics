# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from stattlepy import Stattleship
import json

def player_page(request, player_name): 
	New_query = Stattleship()
	Token = New_query.set_token('46a96fa056bca68ddb8835f70ad68974')
	player_id = "nba-%s" % player_name
	output = New_query.ss_get_results(sport='basketball',league='nba', season_id='nba-2016-2017', ep='player_season_stats',player_id=player_id)
	ppg = output[0]['player_season_stats'][0]['average_points']
	apg = output[0]['player_season_stats'][0]['average_assists']
	rpg = output[0]['player_season_stats'][0]['average_rebounds']
	template = loader.get_template('player/index.html')
	context = {
		'player_name' : player_name,
		'output': output[0]['player_season_stats'],
		'ppg' : ppg,
		'apg' : apg,
		'rpg' : rpg,
	}
	return HttpResponse(template.render(context, request))
