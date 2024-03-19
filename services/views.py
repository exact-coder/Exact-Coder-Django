from django.shortcuts import render
from services.models import Services

# Create your views here.

def services(request):
    services = Services.objects.prefetch_related().filter(status="visible")
    context = {
        'services':services
    }
    return render(request,'pages/services.html',context)