# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from populate_db import  get_team_dict
# Create your views here.
def teams_list(request): 
	template = loader.get_template('team/list.html')
	teams = get_team_dict()
	print "TEAMS %s" % (teams)
	context = {
		'teams' : teams,
	}
	return HttpResponse(template.render(context, request))


def team_page(request, team_slug): 
	template = loader.get_template('../assets/bootstrap-dashboard/index.html')
	teams = get_team_dict()
	name = teams[team_slug]
	context = {
		'team_name' : name,
		'team_slug' : team_slug,
	}
	return HttpResponse(template.render(context, request))

