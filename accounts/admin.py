from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# from accounts.models import User,UserProfile
from django.utils.html import format_html
from accounts.models import Employee,Reader,Administrator,Moderator

# Register your models here.




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['pkid','id','email','username','UserType','is_superuser','is_staff','is_verified','display_image']
    list_display_links = ['id',"email"]
    list_per_page=25
    
    def display_image(self, obj):
        return format_html('<img src="{}" width="35" height="35" />'.format(obj.avator.url))

    display_image.allow_tags = True
    display_image.short_description = 'User Profile Image'

@admin.register(Moderator)
class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['pkid','id','email','username','UserType','is_superuser','is_staff','is_verified','display_image']
    list_display_links = ['id',"email"]
    list_per_page=25

    def display_image(self, obj):
        return format_html('<img src="{}" width="35" height="35" />'.format(obj.avator.url))

    display_image.allow_tags = True
    display_image.short_description = 'User Profile Image'

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ['pkid','id','email','username','UserType','is_superuser','is_staff','is_verified','display_image']
    list_display_links = ['id',"email"]
    list_per_page=25

    def display_image(self, obj):
        return format_html('<img src="{}" width="35" height="35" />'.format(obj.avator.url))

    display_image.allow_tags = True
    display_image.short_description = 'User Profile Image'

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('pkid','id','email','username','UserType','is_superuser','is_staff','is_verified','display_image',)
    list_display_links = ['id',"email"]
    list_per_page=25

    def display_image(self, obj):
        return format_html('<img src="{}" width="35" height="35" />'.format(obj.avator.url))

    display_image.allow_tags = True
    display_image.short_description = 'User Profile Image'
