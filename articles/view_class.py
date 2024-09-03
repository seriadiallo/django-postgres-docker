from typing import Any
from django.views.generic import ListView, View, CreateView, DetailView
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse

from .models import Article
from .forms import ArticleForm, CommentForm


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    # template_name = 'articles/list-articles.html'
    queryset = Article.objects.filter(date_pub__lte=timezone.now())


class ArticleCreateView(CreateView):
    model = Article
    # fields = ('title', 'sumary', 'cover', 'date_pub', 'content')
    form_class = ArticleForm
    template_name = 'articles/formulaire.html'




# class ArticleCreateView(View):
#     def get(self, request):
#         form = ArticleForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'articles/formulaire.html', context)

#     def post(self, request):
#         form = ArticleForm(request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()  # enregistrement dans la base
#             return redirect(reverse('list-articles'))
#         context = {
#             'form': form
#         }
#         return render(request, 'articles/formulaire.html', context)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
