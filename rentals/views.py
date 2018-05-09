# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from core.forms.galleryform import PhotoGalleryForm
from core.models import Gallery
from rentals.forms.hotel import HotelForm
from rentals.models import City, Hotel


def cities_list(request):

    cities = City.objects.all().prefetch_related('hotels')
    return render(request, 'cities/list.html', {
        'cities': cities
    })

def hotel_detail(request, pk, slug=None):
    hotel = get_object_or_404(Hotel, pk=pk)
    can_edit = request.user == hotel.owner

    if not hotel.gallery:
        hotel.gallery = Gallery.objects.create()
        hotel.save()

    gallery = hotel.gallery.photos.all()

    return render(request, 'hotels/detail.html', {
        'hotel': hotel,
        'can_edit_hotel': can_edit,
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

@login_required
def hotel_owner_edit(request):
    hotel = Hotel.objects.filter(owner=request.user).first()
    return redirect('hotel_edit', pk=hotel.pk)

@login_required
def hotel_owner_rentals(request):
    hotel = Hotel.objects.filter(owner=request.user).first()
    return redirect('hotel_rentals', pk=hotel.pk)

@login_required
def hotel_rentals(request, pk):
    return render(request, 'rentals/hotel_list.html', {
})


@login_required
def hotel_edit(request, pk):

    hotel = get_object_or_404(Hotel, pk=pk)
    gallery = hotel.gallery
    can_edit = request.user.is_superuser or request.user == hotel.owner

    if not can_edit:
        return redirect('hotel_detail', pk=hotel.pk )

    gallery_factory = PhotoGalleryForm.getGalleryFormset(gallery)
    initial_photos = PhotoGalleryForm.get_initial(gallery)

    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        gallery_formset = gallery_factory(request.POST, request.FILES, initial=initial_photos)

        if form.is_valid() and gallery_formset.is_valid():

            hotel = form.save(commit=False)
            if gallery is None:
                gallery = Gallery.objects.create()
            hotel.gallery = gallery
            hotel.save()
            form.save_m2m()

            PhotoGalleryForm.save_galleryphoto(hotel.gallery, gallery_formset)

            return redirect('hotel_detail', pk=hotel.pk, slug=hotel.slug)
        else:
            print form.errors.as_data()
            print gallery_formset.errors
    else:
        form = HotelForm(instance=hotel)
        gallery_formset = gallery_factory(initial=initial_photos)


    return render(request, 'hotels/edit.html', {
        'form': form,
        'gallery_formset':gallery_formset,
        'hotel': hotel,
        'can_edit_hotel':can_edit
    })
