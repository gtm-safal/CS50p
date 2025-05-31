# test_project.py
import pytest
from project import add_movie, get_movie_info, load_movies, list_movies, save_movies

def test_add_movie(tmp_path):
    test_file = tmp_path / "movies.csv"
    movies = []
    save_movies(movies, test_file)  # Create an empty CSV

    movies = load_movies(test_file)
    assert add_movie(movies, "Test Movie", "Test Director", 2022, 8.5, test_file) == True
    # Reload to verify persistency
    movies = load_movies(test_file)
    assert add_movie(movies, "Test Movie", "Test Director", 2022, 8.5, test_file) == False  # Duplicate

def test_get_movie_info(capsys):
    movies = [
        {"name": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 9.0}
    ]
    get_movie_info(movies, 0)
    captured = capsys.readouterr()
    assert "Interstellar" in captured.out
    assert "Christopher Nolan" in captured.out

def test_list_movies(capsys):
    movies = [
        {"name": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 9.5},
        {"name": "The Matrix", "director": "Wachowskis", "year": 1999, "rating": 8.7}
    ]
    list_movies(movies)
    captured = capsys.readouterr()
    assert "1. Inception" in captured.out
    assert "2. The Matrix" in captured.out
