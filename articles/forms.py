from django import forms

from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(min_length=2, max_length=255)
#     sumary = forms.CharField(min_length=2, max_length=255, required=False)
#     date_pub = forms.DateField(required=False, widget=forms.DateInput())
#     content = forms.CharField(widget=forms.Textarea(attrs={'required': True}))

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'sumary', 'date_pub', 'content')
