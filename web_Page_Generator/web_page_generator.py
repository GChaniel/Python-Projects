
import tkinter as tk
from tkinter import *
import os
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)

        #Set title of GUI window
        self.master.title("Web Page Generator")

        #Text Heading Label
        self.lbl_heading = tk.Label(self.master, text='Enter custom text or click Default HTML page button')
        self.lbl_heading.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(20, 0), sticky="w")

        #Creates entry text and position
        self.entry_text = Entry(self.master, width=60, bg="grey")
        self.entry_text.grid(row=2, column=0, columnspan=2, padx=(20,10), pady=(10, 0), sticky="ew")

        #Create a button that generate a default HTML    
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column=0, padx=(10,10), pady=(10,10))

        #Create a button that submit Custom text    
        self.custom_btn = Button(self.master, text ="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=3, column=1, padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tunned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("file://" + os.path.realpath ("index.html"))

    def customHTML(self):
        customText = self.entry_text.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("file://" + os.path.realpath ("index.html"))




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
