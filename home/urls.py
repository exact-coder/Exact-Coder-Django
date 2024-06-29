from django.urls import path
from home.views import home,contacts,faq,support_chat

urlpatterns = [
    path("",home,name="home"),
    path("contacts/",contacts,name="contacts"),
    path("faq/",faq,name="faq"),
    path("support_chat/",support_chat,name="support_chat"),
]
