from django.shortcuts import render
from services.models import Services
from home.models import BreadCrumb

# Create your views here.

def services(request):
    services = Services.objects.prefetch_related().filter(status="visible")
    bread_crumb = BreadCrumb.objects.filter(page_type="SERVICES",type_check="SHOW").first()

    context = {
        'services':services,
        'bread_crumb':bread_crumb,
    }
    return render(request,'pages/services.html',context)