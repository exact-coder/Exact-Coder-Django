from django.urls import path
from home.views import home,contacts,profile

urlpatterns = [
    path("",home,name="home"),
    path("profile/",profile,name="profile"),
    path("contacts/",contacts,name="contacts"),
]
