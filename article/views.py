from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from article.models import Article,ArticleCategory
from django.http import JsonResponse

# Create your views here.

def articles(request):
    categories = ArticleCategory.objects.all()
    articles_obj = Article.objects.all()
    article_paginator = Paginator(articles_obj,9,orphans=4)
    page_number = request.GET.get('page')
    articles_list = article_paginator.get_page(page_number)
    context ={
        'articles':articles_list,
        'categories':categories,
    }
    return render(request,'pages/articles.html',context)

def article_details(request):
    return render(request,'pages/article_details.html')
