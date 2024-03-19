from django.contrib import admin
from services.models import Services


# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id','service_title','status','updated']
    list_display_links =['id','service_title']

