from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views           # This line is new!

urlpatterns = [
    url(r'^/player_selection$', views.player_selection),     # This line has changed!
    url(r'^/rules$', views.rules),
    url(r'^/player_registration$', views.player_registration),
    url(r'^/register_players$', views.register_players),
    url(r'^.*$', RedirectView.as_view(url='game_setup/player_selection', permanent=False), name='player_selection')
  ]