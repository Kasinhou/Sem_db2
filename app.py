
import tkinter as tk
from tkinter import ttk

import src.db as db
from ui.people_menu import People_menu
from ui.system_group_menu import System_group_menu

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Emergency respond system")
        self.root.geometry("1920x1080")

        # Menu bar
        self.menubar = tk.Menu(root)

        self.menu = tk.Menu(self.menubar, tearoff=0)
        self.menu.add_command(
            label="People",
            command=self.show_people
        )
        self.menu.add_command(
            label="Another menu",
            command=self.show_system_group_menu
        )
        self.menu.add_separator()
        self.menu.add_command(
            label="Exit",
            command=self.root.destroy
        )

        self.menubar.add_cascade(
            label="System",
            menu=self.menu
        )
        self.root.config(menu=self.menubar)

        # Content area for the selected menu
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.pack(fill="both", expand=True)

        self.current_menu = None

    def clear_menu(self):
        """Remove the current menu and its widgets."""
        if self.current_menu is not None:
            self.current_menu.destroy()
            self.current_menu = None

        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_people(self):
        self.clear_menu()

        self.current_menu = ttk.Frame(self.content_frame)
        self.current_menu.pack(fill="both", expand=True)

        People_menu(self.current_menu)

    def show_system_group_menu(self):
        self.clear_menu()

        self.current_menu = ttk.Frame(self.content_frame)
        self.current_menu.pack(fill="both", expand=True)

        System_group_menu(self.current_menu)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()