import uuid
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate,login
from accounts.models import Reader, User

# Create your views here.

# Signup Page View.
def user_signup(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        username= request.POST.get('username')
        firstname= request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        password1= request.POST.get('password1')
        password2= request.POST.get('password2')
        if User.objects.filter(email=email).first():
            messages.info(request, "Already exist this email!!")
            return redirect('/users/signup')
        if User.objects.filter(username=username).first():
            messages.info(request, "This username already taken, Try another one!!")
            return redirect('/users/signup')
        if password1 != password2:
            messages.info(request, "Password Doesn't matched!!")
            return redirect('/users/signup')
        user_uuid = str(uuid.uuid4())
        user_obj = Reader.objects.create(id=user_uuid,email=email,username=username,first_name=firstname,last_name=lastname)
        user_obj.set_password(password1)
        
        user_obj.save()
        # send_mail_after_registration
        send_mail_after_registration(email,username,user_uuid)
        messages.success(request, "Successfully Created. Please, Check Your email for verifications !!")
        return redirect("/")
    return render(request,'pages/signup.html')

def send_mail_after_registration(email,username,id):
    sender = "Your e-mail verification link"
    from_email=settings.EMAIL_HOST_USER
    template = loader.get_template('mail_varification.txt'
    )
    context = {'email':email,'id':id,'username':username}
    message = template.render(context)
    email_send = EmailMultiAlternatives(
        sender,message,from_email,[email]
    )
    email_send.content_subtype = "html"
    email_send.send()
def email_verify(request,username,id):
    try:
        user_obj = User.objects.filter(id=id).first()
        if user_obj:
            if user_obj.is_verified:
                messages.success(request,"Account is already verified!!")
                return redirect("/users/login")
            user_obj.is_verified = True
            user_obj.save()
            messages.success(request,"Successfully verified your account!!")
            return redirect("/users/login")
    except Exception as e:
        messages.error(request,"Something is wrong!!")
        print(e)



# Login Page View.
def user_login(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        password= request.POST.get('password')
        user_obj = User.objects.filter(email=email).first()
        if user_obj is None:
            messages.info(request,"User not Found!!")
            return redirect('/users/login')
        elif not user_obj.is_verified:
            messages.info(request,"Account isnot verified.Check your email for verification!!")
            return redirect('/users/login')
        else:
            if Reader.objects.filter(email=email).first():
                user = authenticate(email=email,password=password)
                if user is None:
                    messages.error(request,"Wrong Password!!")
                    return redirect('/users/login')
                login(request,user)
                return redirect("/profile")



    return render(request,'pages/login.html')

