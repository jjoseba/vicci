from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='index'),
    url(r'^ilmondo/$', views.cities_list, name='cities_list'),
    url(r'^seivicci/$', views.dashboard, name='dashboard'),
    url(r'^seivicci/rentals/$', views.user_rentals, name='user_rentals'),
    url(r'^book/\?hotel=(?P<pk>\d+)$', views.hotel_book, name='hotel_book'),

    url(r'^hotel/edit/$', views.hotel_owner_edit, name='hotel_owner_edit'),
    url(r'^hotel/rentals/$', views.hotel_owner_rentals, name='hotel_owner_rentals'),
    url(r'^hotel/(?P<pk>\d+)/edit/$', views.hotel_edit, name='hotel_edit'),
    url(r'^hotel/(?P<pk>\d+)/rentals/$', views.hotel_rentals, name='hotel_rentals'),
    url(r'^hotel/(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$', views.hotel_detail, name='hotel_detail'),

]