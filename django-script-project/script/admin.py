from django.contrib import admin
from django.forms import Script

from .models import CategoryGroup, Script
# Register your models here.

admin.site.register(CategoryGroup)
admin.site.register(Script)
