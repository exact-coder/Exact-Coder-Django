from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Services(models.Model):
    SERVICES_STATUS = [
        ('visible', 'Visible'),
        ('not visible', 'Not Visible'),
    ]
    service_title = models.CharField(_("Service Title"), max_length=100)
    service_logo = models.ImageField(_("Logo"), upload_to='services/')
    service_description = models.TextField(_("Description"))
    service_banner = models.ImageField(_("Banner"), upload_to='services/')
    updated = models.DateTimeField(_("Created"), auto_now=True, auto_now_add=False)
    status = models.CharField(_("Service Status"), max_length=100,choices=SERVICES_STATUS,default='not visible')

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'
