from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title
