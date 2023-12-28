from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from article.models import Article,ArticleCategory,ArticleSection
from django.http import JsonResponse
from django.template.loader import render_to_string

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
    context = {
        "article": article_obj,
        "article_extra_section":article_section,
        'previous_article': previous_article,
        'next_article': next_article,
    }
    return render(request,'pages/article_details.html',context)

def filter_articles(request):
    categories = request.GET.getlist('category[]')

    allArticles = Article.objects.filter(status='published').order_by('-created').distinct()
    if len(categories) > 0:
        allArticles = allArticles.filter(categories__slug__in=categories).distinct()

    t = render_to_string('ajax/article-filter.html', {'articles': allArticles})

    return JsonResponse({'data': t})
