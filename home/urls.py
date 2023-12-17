from django.urls import path
from home.views import home,contacts

urlpatterns = [
    path("",home,name="home"),
    path("contacts/",contacts,name="contacts"),
]
