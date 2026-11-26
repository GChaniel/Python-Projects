from django.contrib import admin
from .models import UniversityCampus

# Allows administrators to view, add, edit, and delete university campuses.
admin.site.register(UniversityCampus)
