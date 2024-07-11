from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from article.models import Article,ArticleCategory,ArticleSection,ArticleComment,CommentReplay
from django.http import JsonResponse
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from accounts.models import User
from django.contrib import messages

# Create your views here.

def articles(request):
    categories = ArticleCategory.objects.prefetch_related()
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
    article_section = ArticleSection.objects.prefetch_related().filter(article=article_obj)
    categories = article_obj.categories.prefetch_related()
    # Get the previous and next posts
    previous_article = Article.objects.prefetch_related().filter(categories__in=categories, slug__lt=slug).order_by('-id').first()
    next_article = Article.objects.prefetch_related().filter(categories__in=categories, slug__gt=slug).order_by('-created').first()
    article_comment = ArticleComment.objects.prefetch_related('comment_article').filter(comment_article=article_obj).order_by('created')


    commenter = request.user
    if request.method == 'POST' and 'form_submit' in request.POST and request.POST['form_submit'] == 'Comment':
        comment_text = request.POST.get('comment_text')
        if len(comment_text) >= 2:
            if request.user.is_authenticated:
                if commenter:
                    comment = ArticleComment(commenter=commenter,comment_article=article_obj,comment_text=comment_text)
                    comment.save()
                    if request.htmx:
                        comment_htmx = ArticleComment.objects.filter(comment_article=article_obj).last()
                        context = {
                        'comment_htmx':comment_htmx,
                        }
                        comment_html = render_to_string(
                            'components/article/article_single_comment.html',context,request=request
                        )
                    
                        oob_swap_command = (
                            '<div hx-swap-oob="true" hx-request={"timeout":100} id="comment_added" style="margin-bottom:8px;padding:3px;font-size:18px;font-weigth:700;color:green;" >Your Comment Added!</div>'
                        )
                        comment_html+=oob_swap_command
                        return HttpResponse(comment_html)
                    else:
                        messages.error(request, "Something Wrong!! ")
                        return
            else:
                return HttpResponseRedirect(reverse_lazy('login'))
        return HttpResponseRedirect(reverse_lazy("article_details"))

    
    
    replayer = request.user
    if request.method == 'POST' and 'form_submit' in request.POST and request.POST['form_submit'] == 'Replay':
        replay_text = request.POST.get('replay_text')
        comment_id = request.POST.get('comment_id')
        comment_obj = get_object_or_404(ArticleComment,comment_id=comment_id)
        if (len(replay_text) >= 2):
            if request.user.is_authenticated:
                if replayer:
                    replay = CommentReplay(replayer=replayer,replay_comment=comment_obj,replay_text=replay_text)
                    replay.save()
                    if request.htmx:
                        replay_htmx = replay
                        context = {
                        'replay_htmx':replay_htmx,
                        }
                        replay_html = render_to_string(
                            'components/article/single_comment_replay.html',context,request=request
                        )
                        oob_swap_command = (
                            '<div hx-swap-oob="true" hx-request={"timeout":100} id="replay_added" style="margin-bottom:8px;margin-left:8px;padding:3px;font-size:18px;font-weigth:700;color:green;"> Your Replay Added!</div>'
                        )
                        replay_html+=oob_swap_command
                        return HttpResponse(replay_html)
                    else:
                        messages.error(request, "Something Wrong!! ")
                        return
                    # return HttpResponseRedirect(reverse_lazy("article_details"))
            else:
                return HttpResponseRedirect(reverse_lazy('login'))
    
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
    article_slug = comment_obj.comment_article.slug
    article_obj = get_object_or_404(Article,slug=article_slug)
    article_comment = ArticleComment.objects.prefetch_related('comment_article').filter(comment_article=article_obj).order_by('created')
    if request.user.is_authenticated and request.user.email== comment_obj.commenter.email:
        comment_obj.delete()
        context={
            "article": article_obj,
            'comments':article_comment,
        }
        article_html = render_to_string(
            'components/article/comment.html',context,request=request
        )
        return HttpResponse(article_html)
    return HttpResponseRedirect(reverse_lazy("article_details"))

def delete_replay(request,replay_id,slug):
    replay_obj = get_object_or_404(CommentReplay,replay_id=replay_id,slug=slug)
    article_slug = replay_obj.replay_comment.comment_article.slug
    article_obj = get_object_or_404(Article,slug=article_slug)
    article_comment = ArticleComment.objects.prefetch_related('comment_article').filter(comment_article=article_obj).order_by('created')
    if request.user.is_authenticated and request.user.email== replay_obj.replayer.email:
        replay_obj.delete()
        context={
            "article": article_obj,
            'comments':article_comment,
        }
        article_html = render_to_string(
            'components/article/comment.html',context,request=request
        )
        return HttpResponse(article_html)
        # article_slug = replay_obj.replay_comment.comment_article.slug
        # redirect_url = f'/articles/details/{article_slug}'
        # return redirect(redirect_url)
    # return redirect('/articles/details/', slug=replay_obj.replay_article.slug)
    return HttpResponseRedirect(reverse_lazy("article_details"))


def filter_articles(request):
    categories = request.GET.getlist('category[]')

    allArticles = Article.objects.prefetch_related().filter(status='published').order_by('-created').distinct()
    if len(categories) > 0:
        allArticles = allArticles.prefetch_related().filter(categories__slug__in=categories).distinct()

    t = render_to_string('ajax/article-filter.html', {'articles': allArticles})

    return JsonResponse({'data': t})
