from django.urls import path
from protfolio.views import protfolio


urlpatterns = [
    path("",protfolio,name="protfolio"),
]

