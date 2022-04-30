from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('movies/', views.movies_index, name='index'),
path('accounts/signup/', views.signup, name='signup'),
path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
path('movies/<int:movie_id>/add_review/', views.add_review, name='add_review'),
path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
path('movies/search_movies/', views.search_movies, name='search-movies'),
]