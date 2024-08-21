from django.urls import path

from .views import list_article, formulaire

urlpatterns = [
    path('', list_article, name='list-articles'),
    path('ajout/', formulaire, name='form-articles'),
]
