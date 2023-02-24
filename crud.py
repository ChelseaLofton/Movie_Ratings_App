""" CRUD Operations"""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    
    return user

def create_movie(title, overview, release_date, poster_path):
    movie = Movie(
        title = title,
        overview = overview,
        release_date = release_date,
        poster_path = poster_path,
    )

    return movie

def create_rating(user, movie, rating):
    rating = Rating(
        user = user,
        movie = movie,
        rating = rating
    )

    return rating

def get_all_movies():
    
    return Movie.query.all()

if __name__ == "main":
    from server import app
    connect_to_db(app, echo=False)
