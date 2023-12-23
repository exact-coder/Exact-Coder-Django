from django.contrib import admin
from article.models import Article,ArticleSection,Tags,ArticleCategory

# Register your models here.

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display=['tag_name']
    
@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    

class ArticleSectionAdmin(admin.StackedInline):
    model = ArticleSection
    extra =0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','article_main_title','status','author','created','updated']
    list_display_links = ['article_main_title','status']
    inlines =[ArticleSectionAdmin]