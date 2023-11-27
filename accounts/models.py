from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager
from django_resized import ResizedImageField



# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    class UserTypes(models.TextChoices):
        ADMINISTRATOR = "ADMINISTRATOR",'Administrator',
        MODERATOR = "MODERATOR","Moderator",
        EMPLOYEE = "EMPLOYEE","Employee"
        READER = "READER","Reader"

    pkid = models.BigAutoField(primary_key=True,editable=False)
    id = models.UUIDField(_("ID"),default=uuid.uuid4,unique=True)
    username = models.CharField(_("Username"), max_length=100,unique=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(_("Email Address"), max_length=100,unique=True)
    UserType = models.CharField(_("User Type"), max_length=100,choices=UserTypes.choices,default=UserTypes.READER)
    avator = ResizedImageField(_("User Profile Image"),size=[500,500],crop=['middle', 'center'], upload_to="avator/",null=True,blank=True)
    profession = models.CharField(_("Profession"), max_length=50,null=True,blank=True)
    is_verified = models.BooleanField(_("Is Varified"),default=False)
    is_superuser = models.BooleanField(_("Is Superuser"),default=False)
    is_staff = models.BooleanField(_("Is Staff"),default=False)
    is_active = models.BooleanField(_("Is Active"),default=True)
    date_joined = models.DateTimeField(_("User Joined Date"),auto_now=False, auto_now_add=True)

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
    




# Reader user manager
class ReaderUserManager(models.Manager):
    def get_queryset(self,*args, **kwargs) :
        return super().get_queryset(*args,**kwargs).filter(UserType =User.UserTypes.READER)

# Reader proxy user models
class Reader(User):
    objects= ReaderUserManager()
    class Meta:
        proxy = True

    def save(self,*args, **kwargs):
        if not self.id:
            self.UserType = User.UserTypes.READER
        return super().save(*args, **kwargs)

# Employee user manager
class EmployeeUserManager(models.Manager):
    def get_queryset(self,*args, **kwargs) :
        return super().get_queryset(*args,**kwargs).filter(UserType =User.UserTypes.EMPLOYEE)

# Employee proxy user Models
class Employee(User):
    objects= EmployeeUserManager()
    # employeeImage = ResizedImageField(_("Employee Image"),size=[600,600],crop=['middle', 'center'], upload_to="employee/")
    class Meta:
        proxy = True

    def save(self,*args, **kwargs):
        if not self.id:
            self.UserType = User.UserTypes.EMPLOYEE
        return super().save(*args, **kwargs)
    
    def full_name(self):
        return f"{self.first_name + self.last_name}"


# Moderator user manager
class ModeratorUserManager(models.Manager):
    def get_queryset(self,*args, **kwargs) :
        return super().get_queryset(*args,**kwargs).filter(UserType =User.UserTypes.MODERATOR)

    
# Moderator proxy user models
class Moderator(User):
    objects = ModeratorUserManager()
    class Meta:
        proxy = True

    def save(self,*args, **kwargs):
        if not self.id:
            self.UserType = User.UserTypes.MODERATOR
            kwargs.setdefault("is_staff", True)
        return super().save(*args, **kwargs)


# Administrator user manager
class AdministratorUserManager(models.Manager):
    def get_queryset(self,*args, **kwargs) :
        return super().get_queryset(*args,**kwargs).filter(UserType =User.UserTypes.ADMINISTRATOR)

# Administrator proxy user models
class Administrator(User):
    objects = AdministratorUserManager()
    class Meta:
        proxy = True

    def save(self,*args, **kwargs):
        if not self.id:
            self.UserType = User.UserTypes.ADMINISTRATOR
            kwargs.setdefault("is_staff", True)
            kwargs.setdefault("is_superuser",True)
        return super().save(*args, **kwargs)





