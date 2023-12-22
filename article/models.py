from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from autoslug import AutoSlugField
from accounts.models import Reader, User
from ckeditor.fields import RichTextField

# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(_("Tag Name"), max_length=100)

class Article(models.Model):
    ARTICLE_STATUS = [
        ('archived', 'Archived'),
        ('published', 'Published'),
    ]
    article_main_title = models.CharField(_("Main Title"), max_length=120)
    article_sub_title = models.CharField(_("Sub Title"), max_length=200,blank=True,null=True)
    article_banner_img = ResizedImageField(_("Banner Image"),size=[600, 620],upload_to="article_banner",null=True,blank=True)
    article_description = RichTextField(_('Article Description'),config_name='admin_user') # type: ignore
    slug = AutoSlugField(populate_from="article_main_title",unique=True,always_update=True,editable = False)  # type: ignore
    status = models.CharField(max_length=10, choices=ARTICLE_STATUS, default='archived')
    author = models.ForeignKey(User, on_delete=models.CASCADE,editable = False)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)
    tags = models.ManyToManyField(Tags,null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.article_main_title} written by {self.author.username}"

class ArticleSection(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    section_title = models.CharField(_("Article section Title"), max_length=150)
    section_description = RichTextField(_("Article Section Description"),config_name='admin_user') # type: ignore
    
    def __str__(self) -> str:
        return f"{self.article.article_main_title}'s section"