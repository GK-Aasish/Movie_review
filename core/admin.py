from django.contrib import admin
from core.models import Movie,Genre,Reviews

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Reviews)