from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new
from django.views.static import serve


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls,name="admin"),
    path("",include("home.urls")),
    # path('accounts/', include('allauth.urls')),
    path("users/",include("accounts.urls")),
    path("articles/",include("article.urls")),
    path("services/",include("services.urls")),
    path("protfolio/",include("protfolio.urls")),
    path("dashboard/",include("dashboard.urls")),

    # Ckeditor Url
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns = urlpatterns + \
#         static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns = urlpatterns + \
#         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    



