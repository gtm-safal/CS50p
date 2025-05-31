import os
import csv
import argparse

DATA_FILE = "movies.csv"

def clear():    # Clears the  screen
    os.system('cls' if os.name == 'nt' else 'clear')

def load_movies(filename=DATA_FILE):  # Loads movies from the file
    movies = []
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as file:
            pass    # Create the file if it doesn't exist
        return movies

    with open(DATA_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movies.append({
                'name': row['name'],
                'director': row['director'],
                'year': int(row['year']),
                'rating': float(row['rating'])
            })
    return movies

def save_movies(movies, filename=DATA_FILE):    # Saves the list of movies
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'director', 'year', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)

def list_movies(movies):    # Prints a list of all movie
    if not movies:
        print("No movies in the vault.")
        return
    for idx, movie in enumerate(movies, 1):
        print(f"{idx}. {movie['name']}")

def get_movie_info(movies, index):  # Prints  info about a movie
    if 0 <= index < len(movies):
        movie = movies[index]
        print(f"\n🎬 Name     : {movie['name']}")
        print(f"🎞️  Director : {movie['director']}")
        print(f"📅 Year     : {movie['year']}")
        print(f"⭐ Rating   : {movie['rating']}/10\n")
    else:
        print("Invalid index!")

def add_movie(movies, name, director, year, rating, filename=DATA_FILE):    # Adds a new movie
    for movie in movies:
        if movie['name'].lower() == name.lower():
            print("❌ Movie already exists!")
            return False
    movies.append({
        'name': name,
        'director': director,
        'year': year,
        'rating': rating
    })
    save_movies(movies)
    print(f"✅ Added movie: {name}")
    return True

def main():
    parser = argparse.ArgumentParser(description="🎥 MovieVault CLI - Manage your movie collection")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'add' command
    parser_add = subparsers.add_parser("add", help="Add a new movie")
    parser_add.add_argument("--title", required=True, help="Title of the movie")
    parser_add.add_argument("--director", required=True, help="Director of the movie")
    parser_add.add_argument("--year", required=True, type=int, help="Release year")
    parser_add.add_argument("--rating", required=True, type=float, help="Rating out of 10")

    # 'list' 
    parser_list = subparsers.add_parser("list", help="List all movies")

    # 'view' command (corr
    parser_view = subparsers.add_parser("view", help="View info about a movie using index")
    parser_view.add_argument("--index", required=True, type=int, help="Index of the movie (starting from 1)")

    args = parser.parse_args()
    clear()
    movies = load_movies()

    if args.command == "add":
        add_movie(movies, args.title, args.director, args.year, args.rating)
    elif args.command == "list":
        list_movies(movies)
    elif args.command == "view":
        get_movie_info(movies, args.index - 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
