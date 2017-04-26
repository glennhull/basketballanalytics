# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from player.models import Player, Season_Stats, Game_Logs
from team.models import Team
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from stattlepy import Stattleship

def player_page(request, player_name): 
	pname = player_name.replace("-", " ").title()
	pid = Player.objects.filter(player_name=pname).values('player_id')
	ppid = pid[0]['player_id']
	tid = Player.objects.filter(player_name=pname).values('team_id')
	ttid = tid[0]['team_id']
	team_name = Team.objects.filter(team_id = ttid).values('team_name')
	tname = team_name[0]['team_name']
	season_stats = Season_Stats.objects.filter(player_id=ppid)
	# print season_stats
	player = Player.objects.filter(player_name=pname)[:1]
	ppg = season_stats.values('ppg')[0]['ppg']
	apg = season_stats.values('apg')[0]['apg']
	rpg = season_stats.values('rpg')[0]['rpg']
	bpg = season_stats.values('bpg')[0]['bpg']
	spg = season_stats.values('spg')[0]['spg']
	template = loader.get_template('player/index.html')
	context = {
		'player_name' : pname,
		'player' : player,
		'player_id': ppid,
		'output': season_stats,
		'ppg' : ppg,
		'apg' : apg,
		'rpg' : rpg,
		'bpg' : bpg,
		'spg' : spg,
		'team_id': ttid,
		'team_name': tname
	}
	return HttpResponse(template.render(context, request))


