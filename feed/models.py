from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    vote = models.IntegerField(null=True, blank=True, default=0)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    payment = models.BooleanField(default=False)
    reviews = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.title)
