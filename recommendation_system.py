# recommendation_system.py
# Task 4 – Content-Based Recommendation System for CodSoft Internship

# Sample movie dataset
movies = [
    {"title": "The Matrix", "genres": ["action", "sci-fi"]},
    {"title": "Titanic", "genres": ["romance", "drama"]},
    {"title": "The Conjuring", "genres": ["horror", "thriller"]},
    {"title": "Interstellar", "genres": ["sci-fi", "drama"]},
    {"title": "The Notebook", "genres": ["romance", "drama"]},
    {"title": "Avengers", "genres": ["action", "sci-fi"]},
    {"title": "Joker", "genres": ["drama", "thriller"]},
    {"title": "Annabelle", "genres": ["horror"]},
]

# Get user preferences
print("Welcome to the Movie Recommender System!")
user_input = input("Enter your preferred genres (comma-separated, e.g., action, romance): ")

# Convert input to a list and remove spaces
preferred_genres = [genre.strip().lower() for genre in user_input.split(",")]

# Recommendation logic
recommended = []

for movie in movies:
    movie_genres = [genre.lower() for genre in movie["genres"]]
    if any(genre in movie_genres for genre in preferred_genres):
        recommended.append(movie["title"])

# Show results
print("\nRecommended Movies for You:")
if recommended:
    for title in recommended:
        print("🎬", title)
else:
    print("Sorry, no matches found. Try different genres!")
