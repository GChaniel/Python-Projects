# Student Tracking System

A desktop application built with Python, Tkinter and SQLite as part of my Pitman Advanced Web & Software Developer Diploma coursework. It stores student contact details and their current course.

## Features

- Add students with their first name, last name, phone number, email and current course.
- Check that all information fields have been completed before saving.
- View saved records in a table.
- Delete one or multiple selected students after confirmation.
- Keep records in a local SQLite database between sessions.
- Ask for confirmation when closing the application window.

## Technologies Used

- Python 3.
- Tkinter, including `ttk.Treeview` and message boxes.
- SQLite through Python's `sqlite3` module, with parameterized SQL for inserts and deletes.

## Installation and Setup

Clone or download the repository. Use Python 3 with Tkinter and SQLite support and a desktop display. No third-party Python packages are imported by this application.

From the repository root:

```sh
cd Student-tracking
```

## How to Run

```sh
python3 student_main.py
```

On Windows, use `py student_main.py`. Alternatively, open `student_main.py` in Python IDLE and select **Run > Run Module**.

The application automatically creates `students.db` in the current working directory if it does not exist. Run from this project folder to keep the database in a consistent location.

Complete the form and select **Submit Student**. Select one or more rows and choose **Delete Selected** to remove records after confirmation. Use sample student details for demonstrations.

## Project Files

- [student_main.py](student_main.py) — main application window and entry point.
- [student_gui.py](student_gui.py) — interface, form checks and controls.
- [student_func.py](student_func.py) — database functions and exit confirmation.

## What I Learned

- Separating the application window, interface and database functions into modules.
- Connecting Tkinter events to Python functions.
- Creating a SQLite table and inserting, fetching and deleting records.
- Refreshing a table after changes and confirming deletion.

## Known Limitations

- Existing student records cannot be edited through the interface.
- Validation checks for empty fields; it does not validate phone or email formats or prevent duplicate records.
- The application uses a local database and has no user login system.
- No automated tests are included for this project. This documentation review did not run the desktop interface.

[Back to the repository overview](../README.md)
