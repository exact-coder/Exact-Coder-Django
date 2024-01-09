from django.contrib import admin
from django.utils.html import format_html
from home.models import Contacts,Slider

# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id','slider_title','show_or_hide','created','updated']
    list_display_links = ['id','slider_title']

@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','status','_']
    list_display_links = ['name','email']

    # Function to change the icons (Done - Read -Unread)
    def _(self,obj):
        if obj.messagetype == 'SOLVED':
            return True
        else:
            return False
    _.boolean = True

    # Function to color the text (Done - Read - Unread)
    def status(self,obj):
        if obj.messagetype == 'SOLVED':
            color = '#28a745'
        elif obj.messagetype == 'UNREAD':
            color = '#17caf0'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.messagetype))
    status.allow_tags = True

