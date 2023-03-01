<h1> 🔗 URL Shortener APP </h1>

## 📝 Explanation 

This is a 🔵 **Python script** 🔵 that creates a simple GUI application for shortening URLs using the pyshorteners library. The GUI consists of a label and an entry field for entering the URL to be shortened, and a button for triggering the URL shortening process. Once the URL is shortened, a new message box is opened to display the shortened URL, and a "Copy URL" button is provided to copy the shortened URL to the clipboard.

#### The main parts of the code are:

♦ **The URLShortenerGUI class:** This is the main class of the application, which defines the layout and behavior of the GUI.

♦ **The init() method:** This method initializes the GUI by creating the label, entry field, and button widgets and placing them in the appropriate positions using the grid() method.

♦ **The shorten_url() method:** This method is called when the "Shorten URL" button is clicked. It retrieves the URL entered by the user using the get() method of the entry field, and then uses the pyshorteners library to shorten the URL. The shortened URL is then displayed in a new message box using the Toplevel widget. A "Copy URL" button is also added to the message box using the Button widget.

♦ **The copy_url() method:** This method is called when the "Copy URL" button is clicked. It uses the pyperclip library to copy the shortened URL to the clipboard, destroys the message box, and closes the application window.
