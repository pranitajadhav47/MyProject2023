from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Album,Song
# Register your models here

@admin.register(Album)
class AlbumContent(admin.ModelAdmin):
    pass
admin.site.register(Song)
    
