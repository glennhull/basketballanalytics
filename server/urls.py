"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^team/', include('team.urls'), name='team'),
	url(r'^player/', include('player.urls'), name='player'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', TemplateView.as_view(template_name='login/home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'bootstrap-landing/index.html'}, name='logout'),
    url(r'^$', include('index.urls'), name='index')
]


