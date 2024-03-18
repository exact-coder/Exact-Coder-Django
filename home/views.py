from django.shortcuts import render
from protfolio.models import OurWork,Quote
from accounts.models import Employee
from home.models import Contacts,Slider,Faq
from django.contrib import messages
from django.http import HttpResponseRedirect


# Home Page View.
def home(request):
    sliders = Slider.objects.prefetch_related().filter(show_or_hide="SHOW").order_by('-updated')[:10]
    ourworks = OurWork.objects.prefetch_related().order_by('-pkid')[:6]
    employees = Employee.objects.prefetch_related().order_by('-pkid')[:3]
    quotes = Quote.objects.prefetch_related()
    context = {
        'sliders':sliders,
        'ourworks':ourworks,
        'employees':employees,
        'quotes':quotes,
    }
    return render(request,'pages/home.html',context)

def faq(request):
    faqs_obj = Faq.objects.prefetch_related().filter(type_check="SHOW").order_by('-id')
    
    context = {
        "faqs":faqs_obj,
    }
    return render(request, "pages/faq.html",context)


def contacts(request):
    if request.method == 'POST':
        email = request.POST['email']
        # if situation = 'Pending' deny new request
        if Contacts.objects.prefetch_related().filter(email=email, messagetype = "UNREAD").exists():
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
