from django.shortcuts import render
from protfolio.models import OurWork,Quote
from accounts.models import Employee
from home.models import Contacts
from django.contrib import messages
from django.http import HttpResponseRedirect


# Home Page View.
def home(request):
    ourworks = OurWork.objects.all().order_by('-pkid')[:6]
    employees = Employee.objects.all().order_by('-pkid')[:3]
    quotes = Quote.objects.all()
    context = {
        'ourworks':ourworks,
        'employees':employees,
        'quotes':quotes,
    }
    return render(request,'pages/home.html',context)



def contacts(request):
    if request.method == 'POST':
        email = request.POST['email']
        # if situation = 'Pending' deny new request
        if Contacts.objects.filter(email=email, messagetype = "UNREAD").exists():
            messages.info(request,"Already have an Unresponded Message from you !!") 
            return HttpResponseRedirect('/contacts')
        else:
            contact = Contacts()
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            contact.name = name
            contact.email = email
            contact.message = message
            contact.save()
            messages.success(request, 'Messages send Successfully. We will contact with you very soon in your Email !!')
            return HttpResponseRedirect('/')
        

    return render(request, 'pages/contacts.html')
