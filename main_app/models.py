from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

GENRES = (
    ('RC', 'Romantic Comedy'),
    ('TR', 'Thrillers'),
    ('DR', 'Drama'),
    ('CO', 'Comedy'),
    ('DO', 'Documentary'),
    ('FA', 'Family')
)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    movielink = models.CharField(max_length=250)
    genre = models.CharField(
		max_length=2,
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"The user {self.user} has id of {self.id}"