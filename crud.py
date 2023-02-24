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

def get_movie_by_id(movie_id):
    
    movie_by_id = Movie.query.get(movie_id)
    return movie_by_id

def get_all_users():
    
    return User.query.all()

def get_user_by_id(user_id):
    
    user_by_id = User.query.get(user_id)
    return user_by_id

def get_user_by_email(email):

    return User.query.filter(User.email == email).first() 

if __name__ == "main":
    from server import app
    connect_to_db(app, echo=False)


