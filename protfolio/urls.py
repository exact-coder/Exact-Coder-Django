from django.urls import path
from protfolio.views import protfolio,ourWorkDetails,exactCoders


urlpatterns = [
    path("",protfolio,name="protfolio"),
    path("workdetails/<slug:id>/<slug:slug>/",ourWorkDetails,name="workDetails"),
    path("exactCoders/",exactCoders,name="exactCoders"),
]

