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
	template = loader.get_template('../assets/team-dashboard/index.html')
	teams = get_team_dict()
	name = teams[team_slug]
	team_id = Team.objects.filter(team_slug=team_slug).values('team_id')
	roster = get_roster(team_id)
	ppg = get_ppg(team_id)
	apg = get_apg(team_id)
	rpg = get_rpg(team_id)
	bpg = get_bpg(team_id)
	spg = get_spg(team_id)
	fga = get_fga(team_id)
	fgm = get_fgm(team_id)
	tpg = get_tpg(team_id)
	context = {
		'team_name' : name,
		'team_slug' : team_slug,
		'roster' : roster,
		'ppg' : ppg,
		'apg' : apg,
		'rpg' : rpg,
		'bpg' : bpg,
		'spg' : spg, 
		'fga' : fga,
		'fgm' : fgm,
		'tpg' : tpg,
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

def get_ppg(team_id):
	ppg = Team.objects.filter(team_id=team_id).values('ppg')[0]['ppg']
	return ppg

def get_apg(team_id):
	apg = Team.objects.filter(team_id=team_id).values('apg')[0]['apg']
	return apg

def get_rpg(team_id):
	rpg = Team.objects.filter(team_id=team_id).values('rpg')[0]['rpg']
	return rpg

def get_bpg(team_id):
	bpg = Team.objects.filter(team_id=team_id).values('bpg')[0]['bpg']
	return bpg

def get_spg(team_id):
	spg = Team.objects.filter(team_id=team_id).values('spg')[0]['spg']
	return spg

def get_fga(team_id):
	fga = Team.objects.filter(team_id=team_id).values('fga')[0]['fga']
	return fga

def get_fgm(team_id):
	fgm = Team.objects.filter(team_id=team_id).values('fgm')[0]['fgm']
	return fgm

def get_tpg(team_id):
	tpg = Team.objects.filter(team_id=team_id).values('tpg')[0]['tpg']
	return tpg
