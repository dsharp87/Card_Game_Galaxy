from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^/start$', views.start),
    url(r'^/go$', views.go),
  ]