from django.conf.urls import url 
from index import views

app_name = 'index'

urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
]