# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from populate_db import  get_team_dict
from collections import OrderedDict
from team.models import Team
from player.models import Player
# Create your views here.
def teams_list(request): 
	template = loader.get_template('team/list.html')
	teams = OrderedDict(sorted(get_team_dict().items()))
	context = {
		'teams' : teams,
	}
	return HttpResponse(template.render(context, request))


def team_page(request, team_slug): 
	template = loader.get_template('../assets/bootstrap-dashboard/index.html')
	teams = get_team_dict()
	name = teams[team_slug]
	team_id = Team.objects.filter(team_slug=team_slug).values('team_id')
	roster = get_roster(team_id)
	context = {
		'team_name' : name,
		'team_slug' : team_slug,
		'roster' : roster,
	}
	return HttpResponse(template.render(context, request))

# returns dictionary with player name as key and position as value
def get_roster(team_id): 
	roster = {}
	players = Player.objects.filter(team_id=team_id).values('player_name', 'position')
	for p in players: 
		roster[p['player_name']] = p['position']
	ordered_roster = OrderedDict(sorted(roster.items()))
	return ordered_roster
