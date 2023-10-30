from django.urls import path
from protfolio.views import protfolio,exactCoders


urlpatterns = [
    path("",protfolio,name="protfolio"),
    path("exactCoders/",exactCoders,name="exactCoders"),
]

