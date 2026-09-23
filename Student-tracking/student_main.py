# Python Version:   3.14.5
#
# Author:           Isaac GChaniel
#
# Purpose:          Student Tracking System.
#                   A desktop application for adding, viewing, and deleting
#                   student records using Tkinter and SQLite3
#
# Tested OS:        This code was written and tested to with MacOS Tahoe 26.6.2


from tkinter import *
import tkinter as tk

# Import other modules, so we can have access to them.
import student_gui
import student_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Configure the main application window
        self.master = master

        # Set the initial window size and resizing limits.
        self.master.geometry("1000x800")
        self.master.minsize(950, 800)
        self.master.maxsize(1200, 950)

        # Set the window title and background colour.
        self.master.title("Student Tracking")
        self.master.configure(bg="#0D0D0D")

        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on MacOS
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))

        # Load the Student Tracking interface.
        student_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
    
