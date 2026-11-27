# Python & Django Projects

Python and Django coursework, from command-line exercises to desktop applications and database-backed web applications.

## About This Repository

I completed these projects during my **Pitman Advanced Web & Software Developer Diploma** training. This repository brings together the applications and practice exercises that demonstrate the skills I have learned.

These guided coursework projects are intended for local learning and demonstration. Each description focuses on the functionality currently implemented.

## Featured Projects

### [Django Checkbook](Django_Checkbook_Project/)

A web application for creating accounts, recording deposits and withdrawals, and viewing account-specific balance sheets.

- Opening deposits, account selection and running balances ordered by transaction date.
- Django models, model forms, views, URLs, templates and monetary input validation.
- SQLite storage, HTML/CSS styling and 14 automated test methods covering account selection, balances, redirects and form validation. This documentation review did not execute the tests.

**Technologies:** Python, Django, SQLite, HTML, CSS and Bootstrap.

[Setup, usage and limitations](Django_Checkbook_Project/README.md)

### [Student Tracking System](Student-tracking/)

A desktop application for storing student contact details and course information.

- Add and view student records, with checks for missing information.
- Delete one or several selected records after confirmation.
- Store records in SQLite and display them in a Tkinter table.

**Technologies:** Python, Tkinter and SQLite.

[Setup, usage and limitations](Student-tracking/README.md)

### [Django University](DjangoUniversity/)

An administration-based Django project for maintaining university class and campus records.

- Separate models for classes and campuses, with database migrations.
- Add, view, edit and delete records through Django admin.
- Readable model names in the administration interface.

The models are independent; the project has no custom public homepage or class-to-campus relationship.

**Technologies:** Python, Django and SQLite.

[Setup, usage and limitations](DjangoUniversity/README.md)

## Additional Python Projects

| Project | What it demonstrates | Instructions |
| --- | --- | --- |
| [File Transfer Assignment](File%20Transfer%20Assignment/) | A Tkinter interface for selecting folders and moving entries modified within the previous 24 hours. No extension filter or database logging is implemented. | [README](File%20Transfer%20Assignment/README.md) |
| [Web Page Generator](web_Page_Generator/) | A Tkinter interface that writes a default or custom heading to an HTML file and opens it in a browser. | [README](web_Page_Generator/README.md) |
| [Nice or Mean Game](niceOrMeanGame.py) | Functions, loops, conditional statements, input validation, scoring and replay. One help-or-walk-past scenario repeats until either score reaches three. | Run command below. |

## Technical Skills Demonstrated

- **Python fundamentals:** variables, strings, collections, functions, loops and conditional statements.
- **Object-oriented programming:** classes, inheritance, encapsulation conventions and method overriding in the practice exercises.
- **Desktop interfaces:** Tkinter widgets, layouts, event handling, file dialogs, message boxes and table displays.
- **Databases:** SQLite table creation, parameterized SQL, inserting, querying and deleting records.
- **Django:** models, migrations, admin registration, model forms, validation, views, URL routing, templates and database relationships in Checkbook.
- **HTML and CSS:** generated HTML, Django templates, static stylesheets and Bootstrap styling.
- **File handling:** directory entries, modification times, moving files and writing HTML.
- **Input validation:** required student fields, game choices and Django account and transaction forms.
- **Application testing:** Django test cases and assertions for Checkbook behaviour; execution instructions are in its README.

## Python Practice Exercises

- [Inheritance](inheritance_exercise.py): a vehicle parent class with car and motorcycle subclasses.
- [Encapsulation](Encapsulation_Bank_Account.py): a bank-account class using single- and double-underscore attributes and methods for reading and updating a balance.
- [Polymorphism](Polymorphism_assignment.py): animal subclasses overriding a shared method.
- [SQLite and filename filtering](database.py): select `.txt` names from a predefined collection and insert them into SQLite using parameterized SQL and duplicate prevention. This is separate from the File Transfer application.

## Running the Projects

Clone or download this repository, then follow the linked README for the application you want to run. The Django projects each include their own `requirements.txt`; set up a separate virtual environment for each project.

The Tkinter applications require Python 3 with Tkinter and a desktop display. Their READMEs identify the entry script and any files they create.

For Nice or Mean, run this command from the repository root:

```sh
python3 niceOrMeanGame.py
```

On Windows, use `py` in place of `python3`. Follow the terminal prompts to enter a name, choose `N` or `M`, and replay or exit. Scores are kept only during the current session.

Practice scripts can be run from the repository root in the same way. The inheritance exercise defines classes without printing output; `database.py` creates a local `filelist.db` database when run.

## Learning Journey

My coursework has progressed from Python functions, control flow and object-oriented exercises to Tkinter desktop applications and SQLite storage. The Django projects build on those foundations with models, migrations and administration, followed by forms, templates, account-linked transactions and automated test cases.

Together, these projects show the practical skills I have developed so far and provide a foundation for further work on validation, usability and testing.
