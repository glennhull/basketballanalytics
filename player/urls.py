from django.conf.urls import url 
from . import views 

app_name = 'player'

urlpatterns = [
	url(r'^(?P<player_name>.*)', views.player_page, name='player_page'),
]