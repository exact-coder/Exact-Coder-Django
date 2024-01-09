from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField

# Create your models here.

class Slider(models.Model):
    class CheckType(models.TextChoices):
        SHOW = "SHOW",'Show'
        HIDE = "HIDE",'Hide'

    slider_title = models.CharField(_("Slider Title"), max_length=250)
    slider_subtitle = models.CharField(_("Slider Subtitle"), max_length=200,null=True,blank=True)
    slider_image = ResizedImageField(_("Slider Image"),size=[1300,600],crop=['middle', 'center'], upload_to="slider/")
    slider_type = models.CharField(_("Slider Type"), max_length=20,null=True,blank=True)
    button_text = models.CharField(_("Action Button Text"), max_length=20)
    button_link = models.URLField(_("URL of Redirect Page"), max_length=200,null=True,blank=True)
    show_or_hide = models.CharField(_("Show or Hide"), max_length=50,choices=CheckType.choices,default=CheckType.HIDE)
    slug = AutoSlugField(populate_from="slider_title",unique=True) # type: ignore
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)


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

class Faq(models.Model):
    class CheckType(models.TextChoices):
        SHOW = "SHOW",'Show'
        HIDE = "HIDE",'Hide'
    question = models.CharField(_("Question"), max_length=150)
    answer = RichTextField(_('Article Description')) # type: ignore
    slug = AutoSlugField(populate_from="question",unique=True) # type: ignore
    type_check = models.CharField(_("Check Type"), max_length=50,choices=CheckType.choices,default=CheckType.HIDE)