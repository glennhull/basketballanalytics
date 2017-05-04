# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
	template = loader.get_template('../assets/bootstrap-landing/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

@login_required
def dashboard(request):
	template = loader.get_template('../assets/user-dashboard/index.html')
	context = {}
	return HttpResponse(template.render(context, request))	