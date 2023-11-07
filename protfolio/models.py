from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from ckeditor.fields import RichTextField

# Create your models here.
class OurWork(models.Model):
    pkid= models.BigAutoField(primary_key=True,editable=False)
    id= models.UUIDField(_("ID"),default=uuid.uuid4,editable=False,unique=True)
    worktitle = models.CharField(_("Title of the Work"), max_length=100)
    worksubtitle = models.CharField(_("Subtitle of the Work"), max_length=200)
    shortdesc = models.TextField(_("Short Banner Description"),max_length=300)
    workbanner = models.ImageField(_("Work Banner Image"), upload_to="work/")
    workdescription = RichTextField(_("Describe The Work"),config_name='admin_user',null=True,blank=True) # type: ignore
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.worktitle
