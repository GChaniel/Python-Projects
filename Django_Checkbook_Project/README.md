# Django Checkbook Project

A Django checkbook application completed while learning Python with Pitman Training. It lets you create accounts, record deposits and withdrawals, and view each account's balance sheet.

## What the project includes

- Account creation with an opening deposit.
- An account dropdown on the homepage.
- Account-specific balance sheet URLs using a primary key.
- Deposits and withdrawals with running balances.
- Redirection to the account's balance sheet after adding a transaction.
- Validation for required fields and monetary amounts.
- A green banking theme and responsive page layouts.

## Technologies Used

Python, Django, SQLite, HTML, CSS and Bootstrap. Dependencies are listed in [requirements.txt](requirements.txt).

## Requirements

- Python 3.12 or newer.
- pip and Python's `venv` module.
- The dependencies listed in `requirements.txt`.

## Run locally

Clone the repository and open this project:

```sh
git clone https://github.com/GChaniel/Python-Projects.git
cd Python-Projects/Django_Checkbook_Project
```

Create and activate a virtual environment on macOS or Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies, create the database tables, and start the server:

```sh
python -m pip install -r requirements.txt
cd BlueBirdBanking
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/**. Create an account, choose it from the homepage dropdown, and add transactions. Opening deposits can be zero or more; transaction amounts must be at least 0.01. Select **Deposit** or **Withdraw** to determine whether the amount is added or subtracted.

The local SQLite database is excluded from GitHub. A new checkout starts with no accounts or transactions; migrations create the tables, and you add records through the application.

## Check the project

Run these commands from `BlueBirdBanking`, with the virtual environment activated:

```sh
python manage.py check
python manage.py test Checkbook
```

The project includes 14 automated test methods covering account selection, balance calculations, redirects, and form validation. Tests use a separate database. These tests were reviewed but were not executed as part of this documentation update; no passing result is claimed here.

## Project structure

```text
Django_Checkbook_Project/
    README.md
    requirements.txt
    .gitignore
    BlueBirdBanking/
        manage.py
        BlueBirdBanking/    # Project settings and URLs
        Checkbook/         # Models, forms, views, templates, static files, and tests
```

## Development settings

This is a local coursework project using `DEBUG = True`. Set `DJANGO_SECRET_KEY` in your shell to use a consistent local key. If it is unset, Django generates a temporary key for each process. The application does not automatically load `.env` files.

The templates load Bootstrap CSS from a CDN; the main green theme is supplied by the project's local stylesheet.

## What I Learned

- Connecting account and transaction models with a foreign key.
- Processing model forms and displaying validation errors.
- Routing to an account-specific balance sheet and redirecting after submissions.
- Calculating running balances with decimal amounts and ordered transactions.
- Writing Django tests for valid and invalid requests and checking database changes.

## Known Limitations

- This is a local coursework application, without bank integrations or production deployment configuration.
- The account and transaction pages do not require user authentication or enforce ownership of accounts.
- Withdrawals are not checked against available funds, so balances can become negative.
- The web interface does not provide editing or deletion of accounts or transactions.

[Back to the repository overview](../README.md)
