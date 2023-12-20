from django.urls import path
from accounts.views import user_login,user_signup,email_verify,user_logout,ForgetPassword,reset_password

urlpatterns = [
    path("signup/",user_signup,name="signup"),
    path("verify/<str:username>/<slug:id>/",email_verify,name="email_verify"), # type: ignore
    path("login/",user_login,name="login"),
    path("logout/",user_logout,name="logout"),
    path("forget-password/",ForgetPassword,name="forgetPassword"),
    path("reset-password/<slug:token>/",reset_password,name="ResetPassword"), # type: ignore
]


