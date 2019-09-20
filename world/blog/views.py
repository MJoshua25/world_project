from django.shortcuts import render
from .models import *
from faker import Faker
from random import randint
# Create your views here.

def home(request):
    articles_acceuil = Article.objects.filter(article_acceuil=True)[:4]
    category=Category.objects.filter(statut=True)
    article=Article.objects.filter(statut=True)
    data={
        'article_acceuil':articles_acceuil,
        'category':category,
        'article':article,
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


def fa (request):
    arti = Article.objects.all()
    cat = Category.objects.all()
    tag = Tag.objects.all()
    fake = Faker()
    i = 0
    while(i<500):
        art = Article(
            auteur = request.user,
            titre = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
            Description = fake.paragraph(nb_sentences=6, variable_nb_sentences = True, ext_word_list=None),
            contenu = fake.text(max_nb_chars=8000, ext_word_list=None),
            article_acceuil = fake.boolean(chance_of_getting_true=5),
            category_id= cat[randint(1,7)],
            image_cat = arti[randint(1,len(arti)-1)].image_cat,
            image_detail = arti[randint(1,len(arti)-1)].image_detail,
            statut = True
        )
        art.save()
        i+=1