from django.shortcuts import render

# Home Page View.
def home(request):
    return render(request,'pages/home.html')

# Login Page View.
def login(request):
    return render(request,'pages/login.html')

# Signup Page View.
def signup(request):
    return render(request,'pages/signup.html')

def contacts(request):
    return render(request, 'pages/contacts.html')
