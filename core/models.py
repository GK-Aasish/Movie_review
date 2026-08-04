from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name="movies")
    released_date = models.DateField()

    def __str__(self):
        return self.name
    