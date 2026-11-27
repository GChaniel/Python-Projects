# Django University

A Django project for managing university classes and campuses through the Django admin site. It demonstrates how to define database models, create migrations, register models in the admin, and give records readable names.

## What the project includes

- **Classes (`classApp`):** stores a class title, course number, instructor, and duration.
- **Campuses (`campusApp`):** stores a campus name, state code (up to two characters), and campus ID.
- **Django admin:** lets an administrator add, view, edit, and delete these records.
- **SQLite database:** stores data locally without a separate database server.

The two models are independent; there is currently no relationship linking a class to a campus. The application currently exposes only the admin site. A public homepage and custom views have not been implemented.

## Technologies Used

Python, Django and SQLite. Dependencies are listed in [requirements.txt](requirements.txt).

## Requirements

- Python 3.12 or newer.
- pip and Python's `venv` module.
- Django 6.1.3, pinned in `requirements.txt`.

## Run locally

### 1. Get the project

```sh
git clone https://github.com/GChaniel/Python-Projects.git
cd Python-Projects/DjangoUniversity
```

If you already have this project open locally, start from its `DjangoUniversity` directory instead.

### 2. Create and activate a virtual environment

On macOS or Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```sh
python -m pip install -r requirements.txt
```

### 4. Create the database tables

```sh
cd Classes
python manage.py migrate
```

This applies the included migrations and creates `Classes/db.sqlite3`. The database and any existing local records are excluded from GitHub, so a new checkout starts with an empty database.

### 5. Create an administrator account

```sh
python manage.py createsuperuser
```

Follow the prompts to choose your username, email address, and password. You will use this account to sign in to the admin site.

### 6. Start the development server

```sh
python manage.py runserver
```

Open **http://127.0.0.1:8000/admin/** and sign in. Select the class or campus model to add your first records. Use the `/admin/` URL; no custom homepage route is defined.

Press **Ctrl+C** in the terminal to stop the server.

## Project structure

```text
DjangoUniversity/
├── README.md
├── requirements.txt
├── .gitignore
└── Classes/
    ├── manage.py
    ├── Classes/       # Project settings and URL configuration
    ├── classApp/      # UniversityClasses model, admin, and migrations
    └── campusApp/     # UniversityCampus model, admin, and migrations
```

## Useful commands

Run these from the directory containing `manage.py`, with the virtual environment activated:

```sh
python manage.py check          # Check the Django configuration
python manage.py showmigrations # See which migrations have been applied
```

After changing a model, create and apply a migration:

```sh
python manage.py makemigrations
python manage.py migrate
```

## Development settings

`DJANGO_SECRET_KEY` can be set as an environment variable before running Django. If it is unset, the project generates a temporary key for each process. Set a consistent value locally if you want sessions to remain valid across server restarts. Keep your key out of source control. Environment variables must be set in your shell; this project does not automatically load `.env` files.

The current settings use `DEBUG = True` and Django's development server. They are intended for local learning and development. Production deployment requires separate configuration.

## What I Learned

- Defining Django models and creating migrations for database tables.
- Registering models in the admin site for record management.
- Using `__str__` to make records readable in admin lists.
- Setting up a local SQLite database and administrator account.

## Known Limitations

- Classes and campuses are independent models, with no relationship between them.
- Record management is available through Django admin only; custom public views are not implemented.
- The test modules contain starter scaffolding rather than automated test cases. This documentation review did not run the application.
- The settings are intended for local development, as described above.

[Back to the repository overview](../README.md)
