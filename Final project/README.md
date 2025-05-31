# MovieVault

#### Video Demo: [https://youtu.be/ONqbnhZw_e0](https://youtu.be/ONqbnhZw_e0)

---

## Description

**MovieVault** is a command-line Python application that is used to manage a movie collection directly from the terminal. The project allows users to add new movies, list all existing movies, and view information about any saved movie using an index.

The goal of MovieVault is to store movie data in a standard CSV file, making it easy to read & edit. The tool uses Python's `argparse` library for parsing command-line arguments, and ensures data cobvenience with the built-in `csv` module. The project also includes unit tests written using `pytest`, ensuring the functionality.

---

## Project Structure

### `project.py`
This is the main script and the entry point of the application. It defines all core logic for interacting with movies. It includes:
- `load_movies()` — Reads movie data from the CSV file into memory.
- `save_movies()` — Writes the in-memory movie list back into the CSV file.
- `add_movie()` — Adds a new movie to the list after checking for duplicates.
- `list_movies()` — Lists all movies with a numbered index.
- `get_movie_info()` — Displays detailed information about a movie using its index.
- `main()` — Uses `argparse` to process commands (`add`, `list`, `view`) and direct execution accordingly.

### `movies.csv`
This file is created automatically and stores all movies in a structured format (name, director, year, rating).

### `test_project.py`
This file contains unit tests for the `add_movie`, `list_movies`, and `get_movie_info` functions. It uses `pytest` and ensures the functionality

---

## Design Decisions

- **Command-Line Interface**: Using `argparse` provides a clean, intuitive way to interact with the program and scales well if more commands are added later.
- **Testing with `pytest`**: Instead of manually verifying functionality, unit tests improve reliability and ensure that future changes don’t break existing features.
- **Index-Based Access**: Movies are accessed using 1-based indexing for ease of use, matching how users typically count lists.

---

## How to Use

### 1. Add a Movie
```bash
python project.py add --title "Inception" --director "Christopher Nolan" --year 2010 --rating 9.5

```
Adds inception to vault

**2. List all movies:**

```bash
python project.py list
```
Displays the list of all movies with their index numbers.

**2. View Movie Info:**

```bash
python project.py view --index 1
```
Displays the list of all movies with their index numbers.

## Run Tests

```bash
pytest test_project.py
```

