from django.contrib import admin
from .models import *
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","pais","calificacion"]

admin.site.register(Movie,MovieAdmin)
