from django import forms
from .models import Place


class NewPlaceForm(forms.ModelForm):
    """Creates a Form object for entering data in the db.
    from this Django makes the html"""

    class Meta:
        model = Place
        fields = ("name", "visited")
