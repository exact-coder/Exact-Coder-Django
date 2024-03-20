from django.urls import path
from accounts.views import user_login,user_signup,user_logout,forget_password,reset_password,signup_verification

urlpatterns = [
    path("signup/",user_signup,name="signup"),
    # path("verify/<str:username>/<slug:id>/",email_verify,name="email_verify"), # type: ignore
    path("activate/<uidb64>/<token>",signup_verification,name="activate"),
    path("login/",user_login,name="login"),
    path("logout/",user_logout,name="logout"),
    path("forget-password/",forget_password,name="forgetPassword"),
    path("reset-password/<uidb64>/<token>",reset_password,name="ResetPassword"), # type: ignore
]


