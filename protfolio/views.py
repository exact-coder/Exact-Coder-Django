from django.shortcuts import render

# Create your views here.

def protfolio(request):
    return render(request, 'pages/protfolio.html')

def exactCoders(request):
    return render(request, 'pages/exactCoders.html')