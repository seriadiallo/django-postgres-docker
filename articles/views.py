from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ArticleForm, CommentForm
from .models import Article


def list_article(request):
    arts = Article.objects.all()
    context = {
        'articles': arts
    }
    return render(request, 'articles/list-articles.html', context)

@login_required
def formulaire(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()  # enregistrement dans la base
            return redirect(reverse('list-articles'))
        else:
            print(form.errors)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/formulaire.html', context)


def get_and_update(request, id):
    article = Article.objects.get(id=id)  # recuperation d'un article
    if request.method == 'GET':
        form = ArticleForm(instance=article)  # creation d'un formulaire
    elif request.method == 'POST':
        form = ArticleForm(instance=article, data=request.POST, files=request.FILES)  # creation d'un formulaire
        if form.is_valid():
            form.save()
            return redirect(reverse('list-articles'))
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/edit.html', context)


def add_comment(request, id):

    if request.method == 'POST':
        article = Article.objects.get(id=id)
        # initial = {'article': article}
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            context = {
                'article': article,
                'form': form
            }
            return render(request, 'articles/article_detail.html', context)
    return redirect('detail', article.id)

