from django.contrib import admin
from .models import Place

# Register your models here.

# To access admin console, create an admin user
# python manage.py createsuperuser
# http://127.0.0.1:8000/admin

admin.site.register(Place)
