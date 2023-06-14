from tkinter import * 
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pyshorteners

class url_shortner:
       
    def create(self):
        if self.url.get() == "":
            messagebox.showerror("Error","Please Paste an URL")
        else:
            self.urls = self.url.get()
            self.s = pyshorteners.Shortener()
            self.short_url = self.s.tinyurl.short(self.urls)
                        
            self.output = Entry(self.root,font=('Courier',10),fg="black",width=50,relief=FLAT)
            self.output.insert(END,self.short_url)
            self.output.place(x=70,y=120)

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x200')
        self.root.maxsize(600,200)
        self.root.minsize(600,200)
        self.root.title('URL Shortener')
        self.root['bg'] = "white"

        self.title = Label(self.root,text="URL Shortener",font=('Courier',20),bg="white",fg="black")
        self.title.place(x=220,y=10)

        Label(self.root,text="Paste Your URL Here:",font=('Courier',12),bg="white",fg="black").place(x=70,y=60)

        self.url = Entry(self.root,width=50,bg="lightgrey",relief=FLAT)
        self.url.place(x=70,y=90)

        self.button = Button(self.root,text="Create",font=('Courier',12),bg="white",fg="black",command=self.create, relief=FLAT)
        self.button.place(x=480,y=85)
        self.root.mainloop()

if __name__ == '__main__':
    url_shortner()
