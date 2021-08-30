from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class Author(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True, on_delete=CASCADE) 

    def __str__(self):
        return f"{self.title} by {self.author}"
