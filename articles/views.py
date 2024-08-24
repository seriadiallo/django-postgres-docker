from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ArticleForm
from .models import Article


def list_article(request):
    arts = Article.objects.all()
    context = {
        'articles': arts
    }
    return render(request, 'articles/list-articles.html', context)


def formulaire(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # cleaned_data = form.cleaned_data
            # article = Article(**cleaned_data)
            # article.title = cleaned_data['title']
            # article.sumary = cleaned_data['sumary']
            # article.date_pub = cleaned_data['date_pub']
            # article.content = cleaned_data['content']
            form.save()
            return redirect(reverse('list-articles'))
        else:
            print(form.errors)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/formulaire.html', context)
