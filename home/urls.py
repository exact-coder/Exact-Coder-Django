from django.urls import path
from home.views import home,contacts,faq

urlpatterns = [
    path("",home,name="home"),
    path("contacts/",contacts,name="contacts"),
    path("faq/",faq,name="faq"),
]
