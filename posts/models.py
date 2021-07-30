from django.db import models
from django.db.models.base import Model

# Create your models here.
class viewpost(models.Model):
    name=models.CharField(max_length=35)
    desc=models.TextField()
    new=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
