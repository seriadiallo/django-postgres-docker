from django.db import models

# titre, contenu, date publication, resume


class Article(models.Model):

    title = models.CharField(max_length=255, verbose_name='titre')
    sumary = models.CharField(max_length=255, null=True, blank=True, verbose_name='resume')
    content = models.TextField(verbose_name='contenu')
    date_pub = models.DateField(null=True, verbose_name='date de publication')
    cover = models.ImageField(upload_to='articles', max_length=255, null=True, verbose_name="photo de couverture")

    def __str__(self):
        return self.title
