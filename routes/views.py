# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from core.models import Gallery
from rentals.models import Hotel, City
from routes.models import HotelRoute, HotelRoutePoint, RoutePoint, Category


def hotel_routes(request, pk, slug=None):
    hotel = get_object_or_404(Hotel, pk=pk)
    routes = HotelRoute.objects.filter(hotel=hotel)

    if not hotel.gallery:
        hotel.gallery = Gallery.objects.create()
        hotel.save()

    gallery = hotel.gallery.photos.all()

    return render(request, 'routes/hotel_list.html', {
        'hotel': hotel,
        'routes': routes,
        'gallery': gallery,
    })


def route_detail(request, pk):

    route = get_object_or_404(HotelRoute, pk=pk)
    route_points = HotelRoutePoint.objects.filter(hotel_route=route).select_related('route_point')

    return render(request, 'routes/route_detail.html', {
        'route': route,
        'route_points': route_points,
    })

def davicci(request):

    cities = City.objects.all().prefetch_related('hotels')

    return render(request, 'routes/davicci.html', {
        'cities': cities,
    })

def momenti(request):


    return render(request, 'routes/momenti.html', {
    })

def create_personal_hotel_route(request, pk):

    hotel = get_object_or_404(Hotel, pk=pk)
    route_points = RoutePoint.objects.filter(city=hotel.city)
    categories = Category.objects.all()

    return render(request, 'routes/create_route.html', {
        'hotel': hotel,
        'create_personal': True,
        'categories':categories,
        'route_points': route_points,
    })
