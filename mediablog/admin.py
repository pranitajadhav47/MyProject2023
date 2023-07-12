from django.contrib import admin
from .models import blogcontain
# Register your models here

@admin.register(blogcontain)
class blogcontent(admin.ModelAdmin):
    search_fields=['title']
    list_filter=['title']
    list_display =['title','author']
