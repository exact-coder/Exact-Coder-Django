from django.shortcuts import render
from protfolio.models import OurWork,Quote
from accounts.models import Employee

# Create your views here.

def protfolio(request):
    ourwork = OurWork.objects.all()
    context = {
        "ourworks" : ourwork,
    }
    return render(request, 'pages/protfolio.html',context)

def exactCoders(request):
    quotes = Quote.objects.all()
    employees = Employee.objects.all()
    context ={
        'employees' : employees,
        'quotes': quotes,
    }
    return render(request, 'pages/exactCoders.html',context)