

import sqlite3
from tkinter import ttk, messagebox

# This catches if the user's clicks on the 'X' close icon on the upper left to ensure they want to close
def ask_quit(self):
    confirm = messagebox.askokcancel (
        "Exit student Tracking",
        "Are you sure you want to close the student Tracking?"
    )

    if confirm:
        self.master.destroy()

def create_db(self):
    # Connect to the student database.
    conn = sqlite3.connect("students.db") 

    # Create a student table if it doesn't exist.
    with conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
            )
        """)
        conn.commit()
    conn.close()

def fetch_students(self):
    # Connect to the student database
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

     # Retrieve all students records
    cursor.execute("""
        SELECT id, first_name, last_name, phone, email, course
        FROM students
    """)

    students = cursor.fetchall()
    
    conn.close()
    
    return students


def add_student(self, first_name, last_name, phone, email, course):
    # Connect to the student database
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO students (
            first_name, last_name, phone, email, course
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (first_name, last_name, phone, email, course)
    )

    conn.commit()
    conn.close()

def delete_student(self, student_id):
    # Connect to the student database
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # Delete students using their unique ID
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()
