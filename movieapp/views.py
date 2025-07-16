from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.contrib import messages

from .models import Movie, Review
from .forms import ReviewForm


# Home Page View (shows all movies with average ratings)
def home(request):
    movies = Movie.objects.all()
    movie_data = []

    for movie in movies:
        avg_rating = Review.objects.filter(movie=movie).aggregate(Avg('rating'))['rating__avg']
        movie_data.append({
            'movie': movie,
            'avg_rating': round(avg_rating, 1) if avg_rating else 'No ratings yet'
        })

    return render(request, 'movieapp/home.html', {'movie_data': movie_data})


# Movie Detail Page + Review Submission
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie).order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            if Review.objects.filter(user=request.user, movie=movie).exists():
                messages.warning(request, "You have already reviewed this movie.")
            else:
                comment = request.POST.get('comment', '').strip()
                rating = request.POST.get('rating', '').strip()

                if comment and rating:
                    Review.objects.create(
                        movie=movie,
                        user=request.user,
                        comment=comment,
                        rating=int(rating)
                    )
                    messages.success(request, "Review submitted successfully.")
                    return redirect('movie_detail', movie_id=movie.id)
        else:
            messages.error(request, "You must be logged in to submit a review.")
            return redirect('login')

    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'movieapp/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1) if avg_rating else 'No ratings yet'
    })


# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'movieapp/signup.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'movieapp/login.html', {'form': form})


# Logout View
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


# Optional: Dashboard View to show logged-in user's reviews
@login_required
def user_dashboard(request):
    user_reviews = Review.objects.filter(user=request.user).select_related('movie')
    return render(request, 'movieapp/dashboard.html', {
        'user': request.user,
        'reviews': user_reviews
    })
