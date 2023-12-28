import uuid
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
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
            messages.info(request, f"{email} already exist this email!!")
            return redirect('/users/signup')
        if User.objects.filter(username=username).first():
            messages.info(request, f"{ username } username already taken, Try another one!!")
            return redirect('/users/signup')
        if password1 != password2:
            messages.info(request, "Password Doesn't matched!!")
            return redirect('/users/signup')
        user_uuid = str(uuid.uuid4())
        user_obj = Reader.objects.create(id=user_uuid,email=email,username=username,first_name=firstname,last_name=lastname)
        email_subject ="Your e-mail verification link"
        file_name = "mail_varification"
        root_url = request.build_absolute_uri('/')[:-1]
        user_obj.set_password(password1)
        
        user_obj.save()
        # send_mail_after_registration
        send_email(root_url,email_subject,file_name,email,username,user_uuid)

        messages.success(request, f"{ username } successfully Created. Please, Check Your email for verifications !!")
        return redirect("/")
    return render(request,'pages/signup.html')

def user_logout(request):
    logout(request)
    # messages.info(request,"Loged out!")
    return redirect("/users/login/")

def ForgetPassword(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('forget_pass_email')

            if not User.objects.filter(email=email).first():
                messages.info(request,email + " is not a valid email!!")
                return redirect("/users/forget-password/")
            user_obj = User.objects.get(email=email)
            if not user_obj.is_verified:
                messages.info(request,"Account isnot verified.Check your email for verification!!")
                return redirect('/users/login')
            root_url = request.build_absolute_uri('/')[:-1]
            email_subject ="E-mail for Reset Your Password "
            file_name = "mail_pass_reset"
            username = user_obj.first_name +" "+ user_obj.last_name
            user_uuid = user_obj.id
            send_email(root_url,email_subject,file_name,email,username,user_uuid)
            messages.success(request,"Check Your email for Reset Password!!")
            return redirect("/users/login/")
    except Exception as e:
        print(e)
    return render(request,'pages/forgetPassword.html')

def reset_password(request,token):
    context = {}
    try:
        profile_obj = User.objects.get(id=token)
        context = {"user_id":profile_obj.pkid}
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.info(request,'No user found. Please, Retry!!')
                return redirect("/users/forget-password/")
            if new_password != confirm_new_password:
                messages.info(request,"Password does not matched!")
                return redirect("/users/reset-password/{token}/")
            user_obj = User.objects.get(pkid=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request,"password changed Successfully!!")
            return redirect("/users/login/")
        
        
    except Exception as e:
        print(e)
    return render(request,"pages/resetPassword.html",context)


def send_email(root_url,subject,fileName,email,username,id):
    from_email=settings.EMAIL_HOST_USER
    template = loader.get_template(fileName+'.txt'
    )
    context = {'email':email,'id':id,'username':username,'root_url':root_url}
    message = template.render(context)
    email_send = EmailMultiAlternatives(
        subject,message,from_email,[email]
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
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def user_login(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        password= request.POST.get('password')
        user_obj = User.objects.filter(email=email).first()
        if user_obj is None:
            messages.error(request,f"{email} not Found!!")
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
                return redirect("/dashboard/profile")



    return render(request,'pages/login.html')

