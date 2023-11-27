from django.urls import path
from accounts.views import user_login,user_signup,email_verify

urlpatterns = [
    path("signup/",user_signup,name="signup"),
    path("verify/<str:username>/<slug:id>/",email_verify,name="email_verify"), # type: ignore
    path("login/",user_login,name="login"),
]


