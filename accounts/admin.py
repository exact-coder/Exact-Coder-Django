from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from accounts.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['pkid','id','email','username','UserType','is_superuser','is_staff','is_active']
    list_display_links = ['id',"email"]
    list_per_page=25
    search_fields=["email","UserType"]
