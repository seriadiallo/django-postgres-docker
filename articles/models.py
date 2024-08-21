from django.db import models

# titre, contenu, date publication, resume


class Article(models.Model):

    title = models.CharField(max_length=255)
    sumary = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    date_pub = models.DateField(null=True)

    def __str__(self):
        return self.title


