from django.db import models

# Create your models here.


class Place(models.Model):
    """describes a Place table in the database
    with name and visited columns"""

    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, visited? {self.visited}"
