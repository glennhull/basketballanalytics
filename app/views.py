# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('app/index.html')
	context = {}
	return HttpResponse(template.render(context, request))
	# return HttpResponse("You're at index")

def first(request):
	return HttpResponse("You're at first")