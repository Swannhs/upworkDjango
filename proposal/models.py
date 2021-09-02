from django.db import models

# Create your models here.
from feed.models import Post


class Comment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.name
