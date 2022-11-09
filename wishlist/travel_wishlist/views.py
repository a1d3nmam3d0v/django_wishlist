from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.


# Place.objects is a Manager
## (Manager runs queries, returns QuerySet objects)
### ((QuerySet represents set of objects from the db))


def place_list(request):
    # Create new place
    if request.method == "POST":
        form = NewPlaceForm(request.POST)  # Creating form from data in the request
        place = form.save()  # Creates model object from form
        if form.is_valid():  # Validation against db constraints
            place.save()  # Saves place to db
            return redirect("place_list")  # Reloads home page

    """renders a template called wishlist.html
    only shows places that haven't been visited"""

    places = Place.objects.filter(visited=False).order_by("name")  # Sorted by name
    new_place_form = NewPlaceForm()  # The form object gets rendered into an HTML form
    return render(
        request,
        "travel_wishlist/wishlist.html",
        {"places": places, "new_place_form": new_place_form},
    )


def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, "travel_wishlist/visited.html", {"visited": visited})


def place_was_visited(request, place_pk):
    if request.method == "POST":
        # place = Place.objects.get(pk=place_pk)
        # Tries query if object is found it's returned and place is that object if not it returns 404
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()
    # return redirect('places_visited')
    return redirect("place_list")


def about(request):
    author = "Aiden"
    about = "So many places to go, so many things to see. Keep track of them all."
    return render(
        request, "travel_wishlist/about.html", {"author": author, "about": about}
    )
