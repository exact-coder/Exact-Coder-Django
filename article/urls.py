from django.urls import path
from article.views import articles

urlpatterns = [
    path("",articles,name="articles")
]
