from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from accounts.models import User
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def profile(request):
    user_profile = User.objects.get(email=request.user.email,username=request.user.username)
    if user_profile == request.user:
        if request.method == "POST":
            if 'profile_avator' in request.FILES:
                user_profile.avator = request.FILES['profile_avator']
            user_profile.first_name = request.POST.get('firstName', '')
            user_profile.last_name = request.POST.get('lastName', '')
            user_profile.username = request.POST.get('userName')
            user_profile.profession = request.POST.get('profession','')
            user_profile.phone = request.POST.get('phoneNumber','')
            user_profile.date_of_birth = request.POST.get('dateofbirth','')
            user_profile.biography = request.POST.get('aboutBio','')
            if user_profile.is_dirty():
                user_profile.save()
                messages.success(request,"profile update saved!!")
            return HttpResponseRedirect(reverse_lazy("profile"))
    return render(request,"dashboard/pages/profile_settings.html")

def dashboard(request):
    return render(request, "dashboard/pages/index.html")

def write_article(request):
    return render(request, "dashboard/pages/article_write.html")