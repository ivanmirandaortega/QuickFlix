from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

GENRES = (
    ('Romantic Comedy','RC'),
    ('Thrillers','TR',),
    ('Drama','DR'),
    ('Comedy','CO'),
    ('Documentary','DO'),
    ('Family','FA')
)
class Favorite(models.Model):
    name = models.CharField(max_length=600)
    image = models.CharField(max_length=250)
    genre = models.CharField(
        max_length=15,
        #choices
        choices=GENRES,
        default=GENRES[0][0]
    )
    #foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('favorites', kwargs={'pk': self.id})

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    movielink = models.CharField(max_length=250, default = '')
    movieposter = models.CharField(max_length=250)
    genre = models.CharField(
		max_length=15,
		#choices
		choices=GENRES,
		default=GENRES[0][0]
	)
    def __str__(self):
        return f"The Movie {self.name} has id of {self.id}"

class Review(models.Model):
    comment = models.CharField(max_length=100)
    recommend = models.BooleanField(default=False)
    movies = models.ManyToManyField(Movie)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = '1')

    def __str__(self):
        return f"The user {self.user} has id of {self.id}"

    def get_absolute_url(self):
        return reverse('review_detail', kwargs={'pk': self.id})