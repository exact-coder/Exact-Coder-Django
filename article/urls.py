from django.urls import path
from article.views import articles,article_details,filter_articles

urlpatterns = [
    path("",articles,name="articles"),
    path("details/<slug:slug>",article_details,name="article_details"),
    path('filter-articles',filter_articles,name="filter-data"),
]
