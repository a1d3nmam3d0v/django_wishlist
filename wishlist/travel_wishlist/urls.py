from django.urls import path
from . import views

# empty string path matches the one in urls.py
urlpatterns = [
    path("", views.place_list, name="place_list"),
    path("visited", views.places_visited, name="places_visited"),
    path("place/<int:place_pk>/was_visited",views.place_was_visited,name='place_was_visited'),
    path("about", views.about, name="about"),
]
