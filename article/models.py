from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from autoslug import AutoSlugField
from accounts.models import Reader, User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse
import uuid 

# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(_("Tag Name"), max_length=100)
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "{}s".format(verbose_name)
    
    def __str__(self) -> str:
        return f"{self.tag_name}"



class ArticleCategory(models.Model):
    name = models.CharField(_("Category Name"),max_length=120, unique=True)
    slug = AutoSlugField(populate_from="name",unique=True,always_update=True,editable = False) # type: ignore

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ArticleCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Article(models.Model):
    ARTICLE_STATUS = [
        ('archived', 'Archived'),
        ('published', 'Published'),
    ]
    article_main_title = models.CharField(_("Main Title"), max_length=120)
    article_sub_title = models.CharField(_("Sub Title"), max_length=200,blank=True,null=True)
    # article_banner_img = ResizedImageField(_("Banner Image"),size=[600, 620],upload_to="article_banner",null=True,blank=True)
    article_banner_img = models.ImageField(_("Banner Image"),upload_to="article_banner",null=True,blank=True)

    article_description = RichTextField(_('Article Description'),config_name='admin_user') # type: ignore
    slug = AutoSlugField(populate_from="article_main_title",unique=True,always_update=True,editable = False)  # type: ignore
    status = models.CharField(max_length=10, choices=ARTICLE_STATUS, default='archived')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False)
    categories = models.ManyToManyField(ArticleCategory,default="Any")
    tags = models.ManyToManyField(Tags)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.slug)])

    def __str__(self) -> str:
        return f"{self.article_main_title} written by {self.author.username}"

class ArticleSection(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    section_title = models.CharField(_("Article section Title"), max_length=150)
    section_image = models.ImageField(_("Article Section Image"), upload_to="articles",null=True,blank=True)
    section_description = RichTextField(_("Article Section Description"),config_name='admin_user') # type: ignore
    
    def __str__(self) -> str:
        return f"{self.article.article_main_title}'s section"

class ArticleComment(models.Model):
    commenter = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_article = models.ForeignKey(Article,on_delete=models.CASCADE)
    comment_text =  models.TextField(_("Comment"),max_length=200)
    slug=AutoSlugField(populate_from="comment_text",unique=True,always_update=True) # type: ignore
    comment_id = models.UUIDField(_("comment UUID"),default=uuid.uuid4,unique=True)
    created = models.DateField(_("Created"), auto_now=True, auto_now_add=False)

