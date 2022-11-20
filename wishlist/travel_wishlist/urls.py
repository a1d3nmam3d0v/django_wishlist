from django.urls import path
from . import views

# urls.py is for routing
# a list of urls corresponding to requests made to the app
# each url path is matched with a view

urlpatterns = [
    path("", views.place_list, name="place_list"),
    path("visited", views.places_visited, name="places_visited"),
    path(
        "place/<int:place_pk>/was_visited",
        views.place_was_visited,
        name="place_was_visited",
    ),
    path("place/<int:place_pk>", views.place_details, name="place_details"),
    path("place/<int:place_pk>/delete", views.delete_place, name="delete_place"),
]
