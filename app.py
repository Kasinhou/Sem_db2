
import tkinter as tk

import src.db as db
from ui.people_menu import People_menu

# Create the main window
root = tk.Tk()
root.title("Emergency respond system")
root.geometry("1920x1080")

# Create menu bar
menubar = tk.Menu(root)

# Create System menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="System", menu=file_menu)

root.config(menu=menubar)

p_menu = People_menu(root)


# Start the application
root.mainloop()