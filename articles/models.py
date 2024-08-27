from django.db import models

# titre, contenu, date publication, resume


class Article(models.Model):

    title = models.CharField(max_length=255, verbose_name='titre')
    sumary = models.CharField(max_length=255, null=True, blank=True, verbose_name='resume')
    content = models.TextField(verbose_name='contenu')
    date_pub = models.DateField(null=True, verbose_name='date de publication')

    def __str__(self):
        return self.title
