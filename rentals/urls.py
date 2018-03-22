from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^ilmondo/$', views.cities_list, name='cities_list'),
    url(r'^seivicci/$', views.dashboard, name='dashboard'),
    url(r'^book/\?hotel=(?P<pk>\d+)$', views.hotel_book, name='hotel_book'),
    url(r'^hotel/(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', views.hotel_detail, name='hotel_detail'),
]