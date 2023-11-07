from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class OurWork(models.Model):
    pkid= models.BigAutoField(primary_key=True,editable=False)
    id= models.UUIDField(_("ID"),default=uuid.uuid4,editable=False,unique=True)
    worktitle = models.CharField(_("Title of the Work"), max_length=100)
    worksubtitle = models.CharField(_("Subtitle of the Work"), max_length=200)
    shortdesc = models.TextField(_("Short Banner Description"),max_length=280)
    workbanner = ResizedImageField(_("Work Banner Image"),size=[600,600],crop=['middle', 'center'], upload_to="work/")
    workdescription = RichTextField(_("Describe The Work"),config_name='admin_user',null=True,blank=True) # type: ignore
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.worktitle
