from django.urls import path
from article.views import articles,article_details,filter_articles,delete_comment,delete_replay

urlpatterns = [
    path("",articles,name="articles"),
    path("details/<slug:slug>",article_details,name="article_details"),
    path("delete_comment/<slug:comment_id>/<slug:slug>",delete_comment,name="delete_comment"), # type: ignore
    path("delete_replay/<slug:replay_id>/<slug:slug>",delete_replay,name="delete_replay"), # type: ignore
    path('filter-articles',filter_articles,name="filter-data"),
]
