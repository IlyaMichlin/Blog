from django.db import models
from django.urls import reverse


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles_detail', args=[str(self.id)])
