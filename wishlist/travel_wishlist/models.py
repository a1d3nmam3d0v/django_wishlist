from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

# Create your models here.


class Place(models.Model):
    """describes a Place table in the database
    with name and visited columns"""

    user = models.ForeignKey("auth.User", null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="user_images/", blank=True, null=True)

    def save(self, *args, **kwargs):
        old_place = Place.objects.filter(pk=self.pk).first()
        if (
            old_place and old_place.photo
        ):  # if there is an "old place" and it has a photo
            if (
                old_place.photo != self.photo
            ):  # check if old photo is different than new photo aka photo was changed
                self.delete_photo(old_place.photo)  # delete the old photo

        super().save(*args, **kwargs)  # django's save method

    def delete_photo(self, photo):
        if default_storage.exists(photo.name):
            default_storage.delete(photo.name)

    def delete(self, *args, **kwargs):
        if self.photo:
            self.delete_photo(self.photo)
        super().delete(*args, **kwargs)  # call to super class to execute delete

    def __str__(self):
        photo_str = self.photo.url if self.photo else "no photo"
        notes_str = self.notes[100:] if self.notews else "no notes"
        return f"{self.name}, visited? {self.visited} on {self.date_visited}. Notes: {notes_str}. Photo {photo_str}"
