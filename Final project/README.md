# MovieVault

#### 🎬 Video Demo: [https://youtu.be/ONqbnhZw_e0](https://youtu.be/ONqbnhZw_e0)

---

## 📖 Description

**MovieVault** is a command-line Python application that allows users to manage a personal movie collection directly from the terminal. Designed with simplicity and practicality in mind, the project allows users to add new movies, list all existing movies, and view detailed information about any specific movie using an index-based approach.

The goal of MovieVault is to offer a minimalistic, text-based alternative to graphical movie library applications. It stores movie data in a standard CSV file, making it easy to read, edit, and migrate between systems. The tool uses Python's `argparse` library for parsing command-line arguments, and ensures data persistence with the built-in `csv` module. The project also includes unit tests written using `pytest`, ensuring that the core functions behave correctly under a variety of scenarios.

MovieVault is ideal for beginners who want to explore file I/O, CLI-based applications, and test-driven development in Python, while still providing enough structure and features to feel like a complete and functional tool.

---

## 🗂️ Project Structure

### `project.py`
This is the main script and the entry point of the application. It defines all core logic for interacting with movies. It includes:
- `load_movies()` — Reads movie data from the CSV file into memory.
- `save_movies()` — Writes the in-memory movie list back into the CSV file.
- `add_movie()` — Adds a new movie to the list after checking for duplicates.
- `list_movies()` — Lists all movies with a numbered index.
- `get_movie_info()` — Displays detailed information about a movie using its index.
- `main()` — Uses `argparse` to process commands (`add`, `list`, `view`) and direct execution accordingly.

### `movies.csv`
This file is created automatically and stores all movies in a structured format (name, director, year, rating). It's simple and human-readable, allowing portability and editing without any special tools.

### `test_project.py`
This file contains unit tests for the `add_movie`, `list_movies`, and `get_movie_info` functions. It uses `pytest` and ensures the functionality behaves correctly and robustly. The use of `tmp_path` ensures that tests do not affect the actual `movies.csv` file and instead create temporary files for safe testing.

---

## ⚙️ Design Decisions

- **Command-Line Interface**: Using `argparse` provides a clean, intuitive way to interact with the program and scales well if more commands are added later.
- **Testing with `pytest`**: Instead of manually verifying functionality, unit tests improve reliability and ensure that future changes don’t break existing features.
- **Index-Based Access**: Movies are accessed using 1-based indexing for ease of use, matching how users typically count lists.

---

## 🚀 How to Use

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

## 🧪 Run Tests

```bash
pytest test_project.py
```
Runs all tests.

## 🛠️ Installation Instructions

Before using MovieVault, make sure Python 3 is installed. Then install the required dependencies by running:

```bash
pip install -r requirements.txt
```

The main script `project.py` does not require external libraries apart from `pytest` for testing.

