import email
from pydoc_data.topics import topics
from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    def __str__(self):
        return self.first_name
    def __str__(self):
        return self.last_name
    def __str__(self):
        return self.email