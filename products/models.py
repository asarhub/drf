from django.db import models
from tags.models import Tags
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.BigIntegerField()
    quantity = models.BigIntegerField(default=0)
    tags = models.ManyToManyField(Tags,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


