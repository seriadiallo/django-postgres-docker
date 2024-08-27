from django.urls import path

from .views import list_article, formulaire, get_and_update

urlpatterns = [
    path('', list_article, name='list-articles'),
    path('ajout/', formulaire, name='form-articles'),
    path('edit/<int:id>/', get_and_update, name='edit'),
]
