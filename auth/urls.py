from django.conf.urls import url 
from . import views 

app_name = 'auth'

urlpatterns = [
    url(r'^$', views.teams_list, name='teams_list'),
]