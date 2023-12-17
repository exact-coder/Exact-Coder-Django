from django.urls import path
from dashboard.views import profile

urlpatterns = [
    path("profile/",profile,name="profile"),
]
