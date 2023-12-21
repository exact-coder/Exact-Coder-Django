from django.urls import path
from article.views import articles,article_details

urlpatterns = [
    path("",articles,name="articles"),
    path("article_details",article_details,name="article_details"),
]
