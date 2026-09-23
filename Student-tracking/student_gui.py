

import tkinter as tk
from tkinter import ttk, messagebox

# Import other modules, so we can have access to them.
import student_func

def load_gui(self):
    # Create the main container for our interface.
    self.main_frame = tk.Frame(
        self.master,
        bg="#0D0D0D"
    )
    self.main_frame.pack(fill="both", expand=True, padx=25, pady=20)

    # Create the main application heading
    self.heading = tk.Label(
        self.main_frame,
        text="Student Tracking",
        bg="#0D0D0D", fg="#FFFFFF",
        font=("Helvetica", 26, "bold")
    )

    # Position the heading at the top-left of the container
    self.heading.pack(anchor="w")

    # Create a container for the student information form.
    self.form_frame = tk.Frame(
        self.main_frame,
        bg="#0D0D0D"
    )
    self.form_frame.pack(fill="x", pady=(25, 0))

    # Create section heading
    self.form_heading = tk.Label(
        self.form_frame,
        text="Student Information",
        bg="#0D0D0D", fg="#FFFFFF",
        font=("Helvetica", 16, "normal")
    )
    self.form_heading.pack(anchor="w")

    # Create a container for the student input fields
    self.fields_frame = tk.Frame(
        self.form_frame,
        bg="#0D0D0D"
    )
    self.fields_frame.pack(fill="x", pady=(15, 0))

    # Allow both columns to expand equally
    self.fields_frame.columnconfigure(0, weight=1)
    self.fields_frame.columnconfigure(1, weight=1)

    
    # Create the First Name label and position it in the first column.
    self.lbl_fname = tk.Label(self.fields_frame, text="First name", bg="#0D0D0D", fg="#DDDDDD", font=("Helvetica", 11))
    self.lbl_fname.grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(15, 5))

    # Create the Last Name label and position it in the second column.
    self.lbl_lname = tk.Label(self.fields_frame, text="Last name", bg="#0D0D0D", fg="#DDDDDD", font=("Helvetica", 11))
    self.lbl_lname.grid(row=0, column=1, sticky="w", padx=(8, 0), pady=(15, 5))

    # Create the Phone Number label.
    self.lbl_pnumber = tk.Label(self.fields_frame, text="Phone Number", bg="#0D0D0D", fg="#DDDDDD", font=("Helvetica", 11))
    self.lbl_pnumber.grid(row=2, column=0, sticky="w", padx=(0, 8), pady=(15, 5))

    # Create the Email label.
    self.lbl_email = tk.Label(self.fields_frame, text="Email", bg="#0D0D0D", fg="#DDDDDD", font=("Helvetica", 11))
    self.lbl_email.grid(row=2, column=1, sticky="w", padx=(8, 0), pady=(15, 5))

    # Create the Current Course label.
    self.lbl_course = tk.Label(self.fields_frame, text="Current Course", bg="#0D0D0D", fg="#DDDDDD", font=("Helvetica", 11))
    self.lbl_course.grid(row=4, column=0, sticky="w", padx=(0, 8), pady=(15, 5))



    # Create the First Name input field.
    self.txt_fname = tk.Entry(self.fields_frame, bg="#1A1A1A", fg="#FFFFFF", insertbackground="#FFFFFF", font=("Helvetica", 12), relief="flat")
    self.txt_fname.grid(row=1, column=0, sticky="ew", padx=(0, 8), ipady=8)

    # Create the Last Name input field.
    self.txt_lname = tk.Entry(self.fields_frame, bg="#1A1A1A", fg="#FFFFFF", insertbackground="#FFFFFF", font=("Helvetica", 12), relief="flat")
    self.txt_lname.grid(row=1, column=1, sticky="ew", padx=(8, 0), ipady=8)

    # Create the Phone Number input field.
    self.txt_pnumber = tk.Entry(self.fields_frame, bg="#1A1A1A", fg="#FFFFFF", insertbackground="#FFFFFF", font=("Helvetica", 12), relief="flat")
    self.txt_pnumber.grid(row=3, column=0, sticky="ew", padx=(0, 8), ipady=8)

    # Create the Email input field.
    self.txt_email = tk.Entry(self.fields_frame, bg="#1A1A1A", fg="#FFFFFF", insertbackground="#FFFFFF", font=("Helvetica", 12), relief="flat")
    self.txt_email.grid(row=3, column=1, sticky="ew", padx=(8, 0), ipady=8)

    # Create the Current Course input field.
    self.txt_course = tk.Entry(self.fields_frame, bg="#1A1A1A", fg="#FFFFFF", insertbackground="#FFFFFF", font=("Helvetica", 12), relief="flat")
    self.txt_course.grid(row=5, columnspan=2, sticky="ew", padx=0, ipady=8)

    # Create a submit student button.
    self.btn_submit = tk.Label(
        self.fields_frame,
        text="Submit Student",
        bg="#388344",
        fg="#FFFFFF",
        padx=25,
        pady=12,
        font=("Helvetica", 12, "bold"),
        cursor="hand2"
    )
    self.btn_submit.grid(row=6, column=0, sticky="w", pady=(20,0))

    # Run the Submission function when the control is clicked
    self.btn_submit.bind(
        "<Button-1>",
        lambda event: submit_student(self, event)
    )

    
    # Create a container for the student records section.
    self.records_frame = tk.Frame(
        self.main_frame,
        bg="#0D0D0D"
    )

    # Position the records section below the student form.
    self.records_frame.pack(
        fill="both",
        expand=True,
        pady=(30, 0)
    )


    # Create the Student Records section heading.
    self.records_heading = tk.Label(
        self.records_frame,
        text="Student records",
        bg="#0D0D0D",
        fg="#FFFFFF",
        font=("Helvetica", 16, "normal")
    )
    self.records_heading.pack(anchor="w")

    
    # Initialise the student database.
    student_func.create_db(self)

    
    # Define the columns for the student records table.
    columns = (
        "First name",
        "Last name",
        "Phone",
        "Email",
        "Course"
    )

    # Create the student records table.
    self.student_table = ttk.Treeview(
        self.records_frame,
        columns=columns,
        show="headings",
        selectmode="extended",
        height=4
    )

    # Display the column headings.
    for column in columns:
        self.student_table.heading(column, text=column)

    # Position the table below the Student Records heading.
    self.student_table.pack(
        fill="both",
        expand=True,
        pady=(15, 0)
    )

    # Display student records when the application starts.
    display_students(self)

    
    # Create the Delete Selected control.
    self.btn_delete = tk.Label(
        self.records_frame,
        text="Delete Selected",
        bg="#A63D3D",
        fg="#FFFFFF",
        font=("Helvetica", 12, "bold"),
        padx=25,
        pady=12,
        cursor="hand2"
    )

    # Position the control below the student records table.
    self.btn_delete.pack(
        anchor="w",
        pady=(15, 10)
    )

    
    # Run the deletion function when the control is clicked.
    self.btn_delete.bind(
    "<Button-1>",
    lambda event: delete_selected(self, event)
)

def submit_student(self, event=None):
    # Retrieve student infor`mation from the form.
    first_name = self.txt_fname.get().strip()
    last_name = self.txt_lname.get().strip()
    phone = self.txt_pnumber.get().strip()
    email = self.txt_email.get().strip()
    course = self.txt_course.get().strip()

    # Check that all required fields have been completed.
    if not all([first_name, last_name, phone, email, course]):
        messagebox.showwarning(
            "Missing Information",
            "Please complete all student information fields."
        )
        return
    
    # Save the student information to the database
    student_func.add_student(
        self,
        first_name,
        last_name,
        phone,
        email,
        course,
    )

    
    # Clear the student information form.
    self.txt_fname.delete(0, "end")
    self.txt_lname.delete(0, "end")
    self.txt_pnumber.delete(0, "end")
    self.txt_email.delete(0, "end")
    self.txt_course.delete(0, "end")
    
    # Refresh the student records table.
    display_students(self)

def display_students(self):

    # CLear existing records from the Treeview.
    for item in self.student_table.get_children():
        self.student_table.delete(item)

     # Retrieve all student records from the database.
    students = student_func.fetch_students(self)

    # Display each students in the record table.
    for student in students:
        self.student_table.insert(
            "",
            "end",
            iid=student[0],
            values=student[1:]
        )


def delete_selected(self, event=None):
    # Get the selected student records.
    selected_students = self.student_table.selection()
    
    # Check whether any students have been selected.
    if not selected_students:
        messagebox.showwarning(
            "No Selection",
            "Please select a student to delete."
        )
        return

    
    # Ask for confirmation before deleting.
    confirm = messagebox.askyesno(
        "Confirm Deletion",
        "Are you sure you want to delete the selected student(s)?"
    )

    if not confirm:
        return

    
    # Delete each selected student from SQLite.
    for student_id in selected_students:
        student_func.delete_student(self, student_id)

    # Refresh the student records table.
    display_students(self)
