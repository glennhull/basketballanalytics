from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^(?P<player_name>.*)', views.player_page, name='player'),
]