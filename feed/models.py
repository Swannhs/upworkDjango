from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    vote = models.IntegerField(null=True, blank=True, default=0)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    payment = models.BooleanField(default=False)
    reviews = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.title)
