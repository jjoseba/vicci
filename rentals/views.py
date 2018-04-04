# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from core.models import Gallery
from rentals.models import City, Hotel


def cities_list(request):

    cities = City.objects.all().prefetch_related('hotels')
    return render(request, 'cities/list.html', {
        'cities': cities
    })

def hotel_detail(request, pk, slug=None):
    hotel = get_object_or_404(Hotel, pk=pk)

    if not hotel.gallery:
        hotel.gallery = Gallery.objects.create()
        hotel.save()

    gallery = hotel.gallery.photos.all()

    return render(request, 'hotels/detail.html', {
        'hotel': hotel,
        'gallery': gallery,
    })


def hotel_book(request, pk, slug=None):
    hotel = get_object_or_404(Hotel, pk=pk)

    return render(request, 'hotels/book.html', {
        'hotel': hotel,
    })

@login_required
def dashboard(request):

    return render(request, 'user/dashboard.html', {

    })


@login_required
def user_rentals(request):

    return render(request, 'rentals/user_list.html', {

    })
