import pyshorteners as shr
import tkinter as tk
from tkinter import messagebox
import pyperclip


class URLShortenerGUI:
    def __init__(self, master):
        self.master = master
        master.title("URL Shortener")
        master.resizable(False, False)
        master.configure(background="#FFFFFF")
        
        self.label = tk.Label(master, text="Enter URL:", font=("Arial", 12), bg="#FFFFFF")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.entry = tk.Entry(master, font=("Arial", 12), width=40, bd=2, relief="solid")
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")
        
        self.button = tk.Button(master, text="Shorten URL", font=("Arial", 12), command=self.shorten_url, bg="#007AFF", fg="#FFFFFF")
        self.button.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        
    def shorten_url(self):
        url = self.entry.get()
        shortener = shr.Shortener()
        short_url = shortener.tinyurl.short(url)
        
        # Crea una nueva ventana de mensaje utilizando Toplevel
        message_box = tk.Toplevel(self.master)
        message_box.title("Shortened URL")
        message_box.configure(background="#FFFFFF")
        
        message_text = f"The shortened URL is:\n{short_url}"
        message_label = tk.Label(message_box, text=message_text, font=("Arial", 12), bg="#FFFFFF")
        message_label.pack(padx=10, pady=10)
        
        # Agrega el botón "Copy URL" a la ventana de mensaje
        copy_button = tk.Button(message_box, text="Copy URL", font=("Arial", 12), command=lambda: self.copy_url(short_url, message_box), bg="#007AFF", fg="#FFFFFF")
        copy_button.pack(side="bottom", padx=10, pady=10)
        
    def copy_url(self, url, message_box):
        pyperclip.copy(url) 
        message_box.destroy()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerGUI(root)
    root.mainloop()