from django.contrib import admin

# Register your models here.
# recipes/admin.py
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Recipe)
