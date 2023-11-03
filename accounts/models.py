from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager



# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):

    class UserTypes(models.TextChoices):
        ADMINISTRATION = "ADMINISTRATION",'Administration',
        MODERATOR = "MODERATOR","Moderator",
        READER = "READER","Reader"

    pkid = models.BigAutoField(primary_key=True,editable=False)
    id = models.UUIDField(_("ID"),default=uuid.uuid4,editable=False,unique=True)
    username = models.CharField(_("Username"), max_length=100,unique=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(_("Email Address"), max_length=100,unique=True)

    UserType = models.CharField(_("User Type"), max_length=100,choices=UserTypes.choices,default=UserTypes.ADMINISTRATION)

    is_superuser = models.BooleanField(_("Is Superuser"),default=False)
    is_staff = models.BooleanField(_("Is Staff"),default=False)
    is_active = models.BooleanField(_("Is Active"),default=True)
    date_joined = models.DateTimeField(_("User Joined Date"),default=timezone.now)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS= ["username","first_name","last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    def __str__(self):
        return self.username
    
    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    def get_short_name(self):
        return self.username
    
class ReaderUserManager(models.Manager):
    def get_queryset(self,*args, **kwargs) :
        return super().get_queryset(*args,**kwargs).filter(UserType =User.UserTypes.READER)


class Reader(User):
    objects= ReaderUserManager()
    class Meta:
        proxy = True

class ModeratorUserManager(models.Manager):
    def get_queryset(self,*args, **kwargs) :
        return super().get_queryset(*args,**kwargs).filter(UserType =User.UserTypes.MODERATOR)

    

class Moderator(User):
    objects = ModeratorUserManager()
    class Meta:
        proxy = True


class AdministrationUserManager(models.Manager):
    def get_queryset(self,*args, **kwargs) :
        return super().get_queryset(*args,**kwargs).filter(UserType =User.UserTypes.ADMINISTRATION)

class Administration(User):
    objects = AdministrationUserManager()
    class Meta:
        proxy = True




