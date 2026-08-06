from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

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
        return self.title


class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="reviews")
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField()

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        unique_together = ('movie','user')

    def __str__(self):
        return str(self.user.username + "'s" + "Review of " + self.movie.title)
    