from django.urls import path
from dashboard.views import profile,dashboard

urlpatterns = [
    path("",dashboard,name="dashboard"),
    path("profile/",profile,name="profile"),
]
