from django.shortcuts import render
from protfolio.models import OurWork,Quote
from accounts.models import Employee
from home.models import Contacts,Slider,Faq
from django.contrib import messages
from django.http import HttpResponseRedirect
from validate_email import validate_email
from django.core.mail import send_mail,EmailMultiAlternatives
from os import getenv
from django.conf import settings
import threading

SEND_EMAIL_ADDRESS = getenv('EMAIL_HOST_USER')

# This class works for sending email asyncronously.
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self) :
        self.email.send(fail_silently=False)
    


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
            if not validate_email(email):
                print(email)
                messages.info(request,"Please provide a valid email!")
                return render(request, 'pages/contacts.html')
            else:
                contact.name = name
                contact.email = email
                contact.message = message
                contact.save()
                email_subject = f"Website:Exactcoder: ---->  {email}"
                # send_mail_after_registration
                send_email(email_subject,message,email)
                messages.success(request, 'Messages send Successfully. We will contact with you very soon in your Email !!')
                return HttpResponseRedirect('/')

    return render(request, 'pages/contacts.html')

# Email send to the user email
def send_email(subject,message,email):
    from_email=settings.EMAIL_HOST_USER
    email = EmailMultiAlternatives(
        subject,message,from_email,[from_email]
    )
    email.content_subtype = "html"
    EmailThread(email).start()

