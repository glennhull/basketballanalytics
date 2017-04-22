from django.conf.urls import url 
from . import views 
app_name = 'team'
urlpatterns = [
	url(r'^$', views.teams_list, name='teams_list'),
	url(r'^(?P<team_slug>.*)', views.team_page, name='team_page'),
]