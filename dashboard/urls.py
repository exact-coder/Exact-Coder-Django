from django.urls import path
from dashboard.views import profile,dashboard,write_article

urlpatterns = [
    path("",dashboard,name="dashboard"),
    path("profile/",profile,name="profile"),
    path("write-article/",write_article,name="write_article"),
]
