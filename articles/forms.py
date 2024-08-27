from django import forms

from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(min_length=2, max_length=255)
#     sumary = forms.CharField(min_length=2, max_length=255, required=False)
#     date_pub = forms.DateField(required=False, widget=forms.DateInput())
#     content = forms.CharField(widget=forms.Textarea(attrs={'required': True}))

class ArticleForm(forms.ModelForm):

    # tag = forms.CharField(max_length=240, min_length=2, required=True,
    #                       widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Article
        fields = ('title', 'sumary', 'date_pub', 'content')
        widgets = {
            "content": forms.Textarea(attrs={"cols": 80, "rows": 20}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sumary': forms.TextInput(attrs={'class': 'form-control'}),
            'date_pub': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
