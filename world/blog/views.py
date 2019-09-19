from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    articles_acceuil = Article.objects.filter(article_acceuil=True)
    data = {
        'art_acc': articles_acceuil
    }
    return render(request, 'pages/index.html', data)

def catagory(request):
    return render(request, 'pages/catagory.html')

def contact(request):
    return render(request, 'pages/contact.html')

def regular_page(request):
    return render(request, 'pages/regular-page.html')

def single_blog(request):
    return render(request, 'pages/single-blog.html')