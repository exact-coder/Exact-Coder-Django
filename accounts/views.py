import uuid
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
from accounts.models import Reader, User
import threading
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from accounts.utils import account_activation_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from home.models import BreadCrumb


# Create your views here.


# This class works for sending email asyncronously.
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self) :
        self.email.send(fail_silently=False)
    

# Signup Page functionality.
def user_signup(request):
    bread_crumb = BreadCrumb.objects.filter(page_type="SIGNUP",type_check="SHOW").first()
    context = {
        'bread_crumb':bread_crumb,
    }
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            email= request.POST.get('email')
            username= request.POST.get('username')
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
            user_obj = Reader.objects.create(id=user_uuid,email=email,username=username)
            user_obj.set_password(password1)
            user_obj.is_active=False
            user_obj.save()

            uidb64= urlsafe_base64_encode(force_bytes(user_obj.id))
            root_url = request.build_absolute_uri('/')[:-1]
            link = reverse('activate',kwargs={'uidb64':uidb64,'token':account_activation_token.make_token(user=user_obj)})

            activate_url = root_url + link
            email_subject ="Your e-mail verification link"
            file_name = "mail_varification"
            
            # send_mail_after_registration
            send_email(activate_url,email_subject,file_name,email,username,user_uuid)

            messages.success(request, f"Please, Check Your email for verification !!")
            return redirect("/")
        return render(request,'pages/signup.html',context)

# This function works for email verificition after sign up 
def signup_verification(request,uidb64,token):
    try:
        id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=id)

        if not account_activation_token.check_token(user,token):
            messages.info(request,f'{user.username} , You are already activated')
            return redirect('login')
        
        if user.is_active and user.is_verified:
            return redirect('login')
        user.is_active=True
        user.is_verified=True
        user.save()
        messages.success(request, 'Account Activated successfully')
        return redirect('login')
    except Exception as e:
        messages.error(request,"Something is wrong!!")
        print(e)
    return redirect('login')


# User Logedout
def user_logout(request):
    logout(request)
    # messages.info(request,"Loged out!")
    return redirect("/users/login/")



def forget_password(request):
    bread_crumb = BreadCrumb.objects.filter(page_type="FORGETPASSWORD",type_check="SHOW").first()
    context = {
        'bread_crumb':bread_crumb,
    }
    try:
        if request.method == 'POST':
            email = request.POST.get('forget_pass_email')

            if not User.objects.prefetch_related().filter(email=email).first():
                messages.info(request,email + " is not a valid email!!")
                return redirect("/users/forget-password/")
            user_obj = User.objects.get(email=email)
            if not user_obj.is_verified:
                messages.info(request,"Account isnot verified.Check your email for verification!!")
                return redirect('/users/login')
            root_url = request.build_absolute_uri('/')[:-1]
            uid= urlsafe_base64_encode(force_bytes(user_obj.id))
            token = PasswordResetTokenGenerator().make_token(user=user_obj)
            link = reverse('ResetPassword',kwargs={'uidb64':uid,'token':token})
            reset_url = root_url+link
            print('reset_url',reset_url)

            email_subject ="E-mail for Reset Your Password "
            file_name = "mail_pass_reset"
            username = user_obj.get_full_name
            user_uuid = user_obj.id
            send_email(reset_url,email_subject,file_name,email,username,user_uuid)
            messages.success(request,"Check Your email for Reset Password!!")
            return redirect("/users/login/")
    except Exception as e:
        print(e)
    return render(request,'pages/forgetPassword.html',context)

def reset_password(request,uidb64,token):
    bread_crumb = BreadCrumb.objects.filter(page_type="RESETPASSWORD",type_check="SHOW").first()
    context = {
        'bread_crumb':bread_crumb,
        'uidb64':uidb64,
        'token':token,
    }
    try:
        user_id = force_str(urlsafe_base64_decode(uidb64))
        profile_obj = User.objects.get(id=user_id)

        if not PasswordResetTokenGenerator().check_token(user=profile_obj,token=token):
            messages.info(request, "Password link is already Used, Request for new one")
            return redirect('forgetPassword')

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')

            # user = request.POST.get('user_id')
            # if user is None:
            #     messages.info(request,'No user found. Please, Retry!!')
            #     return redirect("/users/forget-password/")

            if new_password != confirm_new_password:
                messages.info(request,"Password does not matched!")
                return render(request,"pages/resetPassword.html",context)
            if len(new_password) < 6:
                messages.error(request,"Password must be highter then 6 characters")
                return render(request,"pages/resetPassword.html",context)
            try:
                user_id = force_str(urlsafe_base64_decode(uidb64))
                user_obj = User.objects.get(id=user_id)
                user_obj.set_password(new_password)
                user_obj.save()
                messages.success(request,"Password changed successfully. \n Login with new password")
                return redirect("/users/login/")
            except Exception as e:
                messages.info(request,"Something Wrong Happened!!")
                print(e)
    except Exception as e:
        print(e)
    return render(request,"pages/resetPassword.html",context)


# Email send to the user email
def send_email(activate_url,subject,fileName,email,username,id):
    from_email=settings.EMAIL_HOST_USER
    template = loader.get_template(fileName+'.txt'
    )
    context = {'email':email,'id':id,'username':username,'activate_url':activate_url}
    message = template.render(context)
    email = EmailMultiAlternatives(
        subject,message,from_email,[email]
    )
    email.content_subtype = "html"
    EmailThread(email).start()



# Login Page View.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def user_login(request):
    bread_crumb = BreadCrumb.objects.filter(page_type="LOGIN",type_check="SHOW").first()
    context={
        'bread_crumb':bread_crumb
    }
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            email= request.POST.get('email')
            password= request.POST.get('password')
            user_obj = User.objects.prefetch_related().filter(email=email).first()
            if user_obj is None:
                messages.error(request,f"{email} not Found!!")
                return redirect('/users/login')
            elif not user_obj.is_verified:
                messages.info(request,"Account isnot verified.Check your email for verification!!")
                return redirect('/users/login')
            else:
                if User.objects.prefetch_related().filter(email=email).first():
                    user = authenticate(email=email,password=password)
                    if user is None:
                        messages.error(request,"Wrong Password!!")
                        return redirect('/users/login')
                    login(request,user)
                    return redirect("/dashboard/profile")



    return render(request,'pages/login.html',context)

