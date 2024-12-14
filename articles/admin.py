from django.contrib import admin
from .models import Article
# from .forms import ArticleForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'sumary', 'date_pub', 'user', 'created_at')
    date_hierarchy = "date_pub"
    # form = ArticleForm
    # fields = (('title', 'sumary'), ('date_pub', 'user'), 'content', 'cover')
    fieldsets = [
        (
            "BAse",
            {
                "fields": ["title", "sumary", "date_pub", ],
            },
        ),
        (
            "Description",
            {
                "classes": ["collapse"],
                "fields": ["content", "cover"],
            },
        ),
    ]


admin.site.register(Article, ArticleAdmin)
