from django.contrib import admin
from protfolio.models import OurWork,Quote

# Register your models here.

@admin.register(OurWork)
class OurWorkAdmin(admin.ModelAdmin):
    list_display = ['pkid','worktitle','worksubtitle','shortdesc','updated','created']
    list_display_links =['pkid','worktitle']
    list_per_page = 25
    list_filter = ['worktitle','created','updated']
    search_fields = ['worktitle','created']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id','employeeUser','employeeQuote']
    list_display_links =['employeeUser','employeeQuote']
    list_per_page = 25