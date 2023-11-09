from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Contacts(models.Model):
    class MessageType(models.TextChoices):
        UNREAD = "UNREAD",'Unread'
        SOLVED = "SOLVED",'Solved'
        UNSOLVED = "UNSOLVED",'Unsolved'
    name = models.CharField(_("Name"), max_length=70)
    email = models.EmailField(_("Email"), max_length=150)
    messagetype = models.CharField(_("Message Type"), max_length=50,choices=MessageType.choices,default=MessageType.UNREAD)
    message = models.TextField(_("Message"))

    def __str__(self) -> str:
        return self.name