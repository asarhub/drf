from django.db import models

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "tags"

    #It prints string version of an object
    def __str__(self):
        return self.name

