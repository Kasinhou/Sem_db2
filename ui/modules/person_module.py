from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

from ui.modules.module import Module
import src.persons as persons

class Person_modul(Module):

    def __init__(self, root):
        super().__init__(root)
        self.des = ["personal_id_number", "first_name", "last_name"]

    def add(self):
        person = open_form(self.root,"Add Personal Info", [
            ("personal_id_number", "Personal identification number", str),
            ("first_name", "First name", str),
            ("last_name", "Last name", str)
        ])
 
        if(person is None):
            return

        try:
            persons.add_person(person[0], person[1], person[2])
        except Exception as exc:
            messagebox.showerror("Database error", str(exc))
    def edit(self,tree):
        if not self.selected:
            return

        vals = tree.item(self.selected, "values")

        person = open_form(self.root,"Edit Personal Info", [
            ("original_personal_id_number", "Personal identification number (read-only ID)", str),
            ("first_name", "First name", str),
            ("last_name", "Last name", str)
        ], {
            "original_personal_id_number": vals[0],
            "first_name": vals[1],
            "last_name": vals[2]
        })
        if(person is None):
            return

        try:
            persons.update_person(self.selected, person[1], person[2])
            tree.item(self.selected, values=(self.selected, person[1], person[2]))
        except Exception as exc:
            messagebox.showerror("Database error", str(exc))

    def delete(self):
        if not self.selected:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this person?"
        ):
            return

        try:
            persons.delete_person(self.selected)
        except Exception as exc:
            messagebox.showerror("Database error", str(exc))

        self.selected = None

    def load(self):
        return persons.list_persons()