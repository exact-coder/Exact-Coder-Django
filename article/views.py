from django.shortcuts import render

# Create your views here.

def articles(request):
    return render(request,'pages/articles.html')

def article_details(request):
    return render(request,'pages/article_details.html')