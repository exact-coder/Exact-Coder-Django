from django.urls import path
from home.views import home,signup,login,contacts

urlpatterns = [
    path("",home,name="home"),
    path("signup/",signup,name="signup"),
    path("login/",login,name="login"),
    path("contacts/",contacts,name="contacts"),
]
