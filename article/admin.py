from django.contrib import admin
from django.utils.html import format_html
from article.models import Article,ArticleSection,Tags,ArticleCategory,ArticleComment

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
    list_display = ['id','article_main_title','updated','author','status','_']
    list_display_links = ['article_main_title','status']
    inlines =[ArticleSectionAdmin]

    def _(self,obj):
        if obj.status == 'published':
            return True
        else:
            return False
    _.boolean = True

    def status(self,obj):
        if obj.status == 'published':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color,obj.status))
    status.allow_tags = True

@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['commenter','comment_article','comment_text','created']
    list_display_links=['commenter','comment_text']
