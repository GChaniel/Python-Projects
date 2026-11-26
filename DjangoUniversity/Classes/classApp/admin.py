from django.contrib import admin
from .models import UniversityClasses

# Allows administrators to view, add, edit, and delete university classes.
admin.site.register(UniversityClasses)
