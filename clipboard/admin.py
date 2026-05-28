from django.contrib import admin
from .models import Snippet

# This line registers your table with the dashboard
admin.site.register(Snippet)