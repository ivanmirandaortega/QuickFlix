from operator import contains
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from main_app.models import GENRES, Movie, Review, Favorite
from .forms import ReviewForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'myimagebucket28'

def search_movies(request):
  if request.method == "POST":
    searched = request.POST['searched']
    movies = Movie.objects.filter(genre__contains=searched)
    return render(request,
    'movies/search_movies.html',
    {'searched': searched,
    'movies': movies})
  
  else:
    return render(request,
    'movies/search_movies.html',
    {})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', {'movies': movies})

class MovieCreate(LoginRequiredMixin,CreateView):
  model = Movie
  fields = ['name', 'description', 'genre']
  
  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)



def add_review(request, movie_id):

	# create a ModelForm Instance using the data in the request
	form = ReviewForm(request.POST)
	# validate
	if form.is_valid():
  
		# do somestuff
		# creates an instance of out feeding to be put in the database
		# lets not save it yet, commit=False because we didnt add the foreign key
		new_review = form.save(commit=False)
		#look at the note for cat field in the Feeding Model
		new_review.movie_id = movie_id
		new_review.save() # adds the feeding to the database, and the feeding be associated with the cat
		# with same id as the argument to the function cat_id


	return redirect('detail', movie_id=movie_id)

def assoc_review(request, movie_id, review_id):
  Movie.objects.get(id=movie_id).reviews.add(review_id)
  return redirect('detail', movie_id=movie_id)

class ReviewDetail(LoginRequiredMixin,CreateView):
  model = Review
  fields = ['comment', 'recommend']

class ReviewCreate(LoginRequiredMixin,CreateView):
  model = Review
  fields = ['comment', 'recommend']

    # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class ReviewUpdate(LoginRequiredMixin,CreateView):
  model = Review
  fields = ['comment', 'recommend']

class ReviewDelete(LoginRequiredMixin,CreateView):
  model = Review
  # fields = ['comment', 'recommend']
  success_url = '/movies/'

def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    # create an instance of FeedingForm
    review_form = ReviewForm()

    return render(request, 'movies/detail.html', {'movie': movie, 'review_form': review_form,
    
    })

def favorites(request):
	return render(request, 'movies/favorites.html')

