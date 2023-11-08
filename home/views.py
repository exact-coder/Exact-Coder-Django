from django.shortcuts import render
from protfolio.models import OurWork


# Home Page View.
def home(request):
    ourworks = OurWork.objects.all().order_by('-pkid')[:6]
    context = {
        'ourworks':ourworks,
    }
    return render(request,'pages/home.html',context)

# Login Page View.
def login(request):
    return render(request,'pages/login.html')

# Signup Page View.
def signup(request):
    return render(request,'pages/signup.html')

def contacts(request):
    return render(request, 'pages/contacts.html')
