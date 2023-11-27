from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# from accounts.models import User,UserProfile
from accounts.models import Employee,Reader,Administrator,Moderator

# Register your models here.




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['pkid','id','email','username','UserType','is_superuser','is_staff','is_verified','avator']
    list_display_links = ['id',"email"]
    list_per_page=25
@admin.register(Moderator)
class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['pkid','id','email','username','UserType','is_superuser','is_staff','is_verified','avator']
    list_display_links = ['id',"email"]
    list_per_page=25
@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ['pkid','id','email','username','UserType','is_superuser','is_staff','is_verified','avator']
    list_display_links = ['id',"email"]
    list_per_page=25

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['pkid','id','email','username','UserType','is_superuser','is_staff','is_verified','avator']
    list_display_links = ['id',"email"]
    list_per_page=25
