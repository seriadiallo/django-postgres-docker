from django.urls import path

from .views import list_article, formulaire, get_and_update, add_comment
from .view_class import ArticleListView, ArticleCreateView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='list-articles'),
    path('class/', ArticleListView.as_view(), name='list-articles-class'),
    path('ajout/', formulaire, name='form-articles'),
    path('ajout-class/', ArticleCreateView.as_view(), name='form-articles-class'),
    path('edit/<int:id>/', get_and_update, name='edit'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('add-comment/<int:id>/', add_comment, name='add-comment'),
]
