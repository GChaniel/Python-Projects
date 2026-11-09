
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        #Sets title of GUI window
        self.master.title("File Transfer")

        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)

        #Positions souce button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 10))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75,bg="grey")

        #Positions entry in GUI using tkinter grid, padx and pady are the same
        # as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30, 0))

        #Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)

        #Positions destination button in GUI using tkinter grid()
        #on the next two under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15, 10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75, bg="grey")

        #Positions entry in GUI using tkinter grid, padx and pady are the same
        # as the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15, 0))

        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)

        #Position transfer file button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Position the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
        
    #Creating function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()

        #The .delete clears the content that is inserted in the entry
        #It allows the path to be inserted into the entry widget properly.
        self.source_dir.delete(0, END)

        #The .insert method inserts the user selection to the source dir entry
        self.source_dir.insert(0, selectSourceDir)

      #Creating function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()

        #The .delete clears the content that is inserted in the entry
        #It allows the path to be inserted into the entry widget properly.
        self.destination_dir.delete(0, END)

        #The .insert method inserts the user selection to the destionation dir entry
        self.destination_dir.insert(0, selectDestDir)

    #Creates function to transfer files from one directory to another
    def transferFiles(self):

        #Gets source directory
        source = self.source_dir.get()

        #Gets destination directory
        destination = self.destination_dir.get()

        #Gets a list of files in the source direftory
        source_files = os.listdir(source)

        ##Calculates the cutoff time for files modified within the last 24 hours
        current_time = datetime.now()
        cutoff_time = current_time - timedelta(hours=24)

        #Runs through each files in the source directory
        for i in source_files:
            
            #Gets when last the file was modified 
            modified_time = os.path.getmtime(source + '/' + i)
            file_date = datetime.fromtimestamp(modified_time)

            if file_date >= cutoff_time:
                shutil.move(source + '/' + i, destination)
                print(i + ' was sucessfully transferred.')

            else:
                print(i + ' was skipped because it is older than 24 hours.')

    #Create function to exit the program.
    def exit_program(self):
        root.destroy()

        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


    
