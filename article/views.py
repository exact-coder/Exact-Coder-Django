from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from article.models import Article,ArticleCategory,ArticleSection,ArticleComment
from django.http import JsonResponse
from django.template.loader import render_to_string
from accounts.models import User
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def articles(request):
    categories = ArticleCategory.objects.all()
    articles_obj = Article.objects.filter(status='published').order_by('-created')
    article_paginator = Paginator(articles_obj,9,orphans=4)
    page_number = request.GET.get('page')
    articles_list = article_paginator.get_page(page_number)
    context ={
        'articles':articles_list,
        'categories':categories,
    }
    return render(request,'pages/articles.html',context)

def article_details(request,slug):
    article_obj = get_object_or_404(Article,slug=slug)
    article_section = ArticleSection.objects.filter(article=article_obj)
    categories = article_obj.categories.all()
    # Get the previous and next posts
    previous_article = Article.objects.filter(categories__in=categories, slug__lt=slug).order_by('-id').first()
    next_article = Article.objects.filter(categories__in=categories, slug__gt=slug).order_by('id').first()
    article_comment = ArticleComment.objects.filter(comment_article=article_obj).order_by('-created')

    commenter = request.user
    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        if request.user.is_authenticated:
            if commenter:
                comment = ArticleComment(commenter=commenter,comment_article=article_obj,comment_text=comment_text)
                comment.save()
                redirect_url = f'/articles/details/{slug}'
                messages.success(request, "Your comment added!!")
                return redirect(redirect_url)
        else:
            return redirect('/users/login')
    context = {
        "article": article_obj,
        "article_extra_section":article_section,
        'previous_article': previous_article,
        'next_article': next_article,
        'comments':article_comment,
    }
    return render(request,'pages/article_details.html',context)

def delete_comment(request,comment_id,slug):
    comment_obj = get_object_or_404(ArticleComment,comment_id=comment_id,slug=slug)
    if request.user.is_authenticated and request.user.email== comment_obj.commenter.email:
        article_slug = comment_obj.comment_article.slug
        redirect_url = f'/articles/details/{article_slug}'
        comment_obj.delete()
        return redirect(redirect_url)
    return redirect('/articles/details/', slug=comment_obj.comment_article.slug)


def filter_articles(request):
    categories = request.GET.getlist('category[]')

    allArticles = Article.objects.filter(status='published').order_by('-created').distinct()
    if len(categories) > 0:
        allArticles = allArticles.filter(categories__slug__in=categories).distinct()

    t = render_to_string('ajax/article-filter.html', {'articles': allArticles})

    return JsonResponse({'data': t})
