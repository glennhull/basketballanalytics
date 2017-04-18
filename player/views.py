# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from player.models import Player, Season_Stats, Game_Logs
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from stattlepy import Stattleship

def player_page(request, player_name): 
	pname = player_name.replace("-", " ").title()
	pid = Player.objects.filter(player_name=pname).values('player_id')
	ppid = pid[0]['player_id']
	season_stats = Season_Stats.objects.filter(player_id=ppid)
	print season_stats
	player = Player.objects.filter(player_name=pname)[:1]
	ppg = season_stats.values('ppg')[0]['ppg']
	apg = season_stats.values('apg')[0]['apg']
	rpg = season_stats.values('rpg')[0]['rpg']
	template = loader.get_template('player/index.html')
	context = {
		'player_name' : pname,
		'player' : player,
		'player_id': ppid,
		'output': season_stats,
		'ppg' : ppg,
		'apg' : apg,
		'rpg' : rpg,
	}
	# player_entry_count = Player.objects.filter(player_name = player_name).count()
	# if player_entry_count == 0:
	# 	add_player(player_name)

	return HttpResponse(template.render(context, request))

# def add_player(player_name):
# 	print "adding player"
# 	pl = Player.objects.create(player_name = player_name);	
# 	pl.save()

