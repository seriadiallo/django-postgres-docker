from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=255)
    sumary = forms.CharField(min_length=2, max_length=255, required=False)
    date_pub = forms.DateField(required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'required': True}))
