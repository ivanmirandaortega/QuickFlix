from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('movies/', views.movies_index, name='index'),
path('accounts/signup/', views.signup, name='signup'),
path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
path('movies/<int:movie_id>/add_review/', views.add_review, name='add_review'),
path('movies/<int:pk>/review_delete/', views.review_delete, name='review_delete'),
path('movies/<int:movie_id>/assoc_review/<int:review_id>/', views.assoc_review, name='assoc_review'),
# path('review/create/', views.ReviewCreate.as_view(), name='review_create'),
path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
# path('review/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review_update'),
# path('review/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review_delete'),
path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
path('movies/search_movies/', views.search_movies, name='search-movies'),
path('favorites/', views.favorites, name='favorites'), 
]