from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# titre, contenu, date publication, resume


class Article(models.Model):

    title = models.CharField(max_length=255, verbose_name='titre')
    sumary = models.CharField(max_length=255, null=True, blank=True, verbose_name='resume')
    content = models.TextField(verbose_name='contenu')
    date_pub = models.DateField(null=True, verbose_name='date de publication', default=timezone.now)
    cover = models.ImageField(upload_to='articles', max_length=255, null=True, verbose_name="photo de couverture")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='contenu')
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return f"{self.created_at}"
