from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=100) 
    publication_date = models.DateField()
    pages = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title
