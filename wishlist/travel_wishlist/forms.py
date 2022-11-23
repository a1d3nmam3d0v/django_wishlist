from django import forms
from .models import Place
from django.forms import FileInput, DateInput


class NewPlaceForm(forms.ModelForm):
    """Creates a Form object for entering data in the db.
    from this Django makes the html"""

    class Meta:
        model = Place
        fields = ("name", "visited")


class DateInput(forms.DateInput):
    input_type = "date"


class TripReviewForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ("notes", "date_visited", "photo")
        widgets = {"date_visited": DateInput()}
