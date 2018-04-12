from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^hotel/(?P<pk>\d+)/(?P<slug>[-\w\d]+)/momenti/$', views.hotel_routes, name='hotel_routes'),
    url(r'^momenti/(?P<pk>\d+)/$', views.route_detail, name='route_detail'),
]