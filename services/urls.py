from django.urls import path
from services.views import services

urlpatterns = [
    path("",services,name="services")
]
