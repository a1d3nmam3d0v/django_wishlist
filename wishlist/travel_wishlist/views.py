from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewPlaceForm, TripReviewForm
from .models import Place

# Create your views here.
# A view is a python function that returns a response when a request is made to the app
# it contains the logic of how to respond to each kind of request


# Place.objects is a Manager
## (Manager runs queries, returns QuerySet objects)
### ((QuerySet represents set of objects from the db))


@login_required  # decorator to allow only logged in users
def place_list(request):
    # Create new place
    if request.method == "POST":
        form = NewPlaceForm(request.POST)  # Creating form from data in the request
        place = form.save(commit=False)  # Creates model object from form
        place.user = request.user
        if form.is_valid():  # Validation against db constraints
            place.save()  # Saves place to db
            return redirect("place_list")  # Reloads home page

    """renders a template called wishlist.html
    only shows places that haven't been visited"""

    # with login_required the request object that is passed to each view function contains info about the logged in user
    places = (
        Place.objects.filter(user=request.user).filter(visited=False).order_by("name")
    )  # Sorted by name
    new_place_form = NewPlaceForm()  # The form object gets rendered into an HTML form
    return render(
        request,
        "travel_wishlist/wishlist.html",
        {"places": places, "new_place_form": new_place_form},
    )


@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, "travel_wishlist/visited.html", {"visited": visited})


@login_required
def place_was_visited(request, place_pk):
    if request.method == "POST":
        # place = Place.objects.get(pk=place_pk)
        # Tries query if object is found it's returned and place is that object if not it returns 404
        place = get_object_or_404(Place, pk=place_pk)
        if place.user == request.user:
            place.visited = True
            place.save()
        else:
            return HttpResponseForbidden()
    return redirect("place_list")


@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    # Does place belong to current user?
    if place.user != request.user:
        return HttpResponseForbidden()
    # Is this a GET or POST request?
    # if POST request - validate form data + update Place object
    if request.method == "POST":
        form = TripReviewForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            messages.info(request, "Trip information updated.")
        else:
            messages.error(request, form.errors)
        return redirect("place_details", place_pk=place_pk)
    else:
        # if GET request show place + form
        # if place is visited show form, if not visited no form
        if place.visited:
            review_form = TripReviewForm(instance=place)
            return render(
                request,
                "travel_wishlist/place_detail.html",
                {"place": place, "review_form": review_form},
            )
        else:
            return render(
                request, "travel_wishlist/place_detail.html", {"place": place}
            )


@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect("place_list")
    else:
        return HttpResponseForbidden()
