from django.shortcuts import render
from protfolio.models import OurWork

# Create your views here.

def protfolio(request):
    ourwork = OurWork.objects.all()
    context = {
        "ourworks" : ourwork
    }
    return render(request, 'pages/protfolio.html',context)

def exactCoders(request):
    return render(request, 'pages/exactCoders.html')