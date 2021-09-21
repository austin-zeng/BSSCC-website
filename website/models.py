from django.db import models

class Article(models.Model):
    body_markdown = models.CharField(max_length=40000)
