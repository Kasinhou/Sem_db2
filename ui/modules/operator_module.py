from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

from ui.modules.module import Module
import src.operators as operators

class Operator_modul(Module):

    def __init__(self, root, person_module):
        super().__init__(root)
        self.des = ["operator_id", "system_group_id", "personal_id_number", "username", "role", "active"]
        self.person_modul = person_module

    def add(self):
        if not self.person_modul.selected:
            return

        operator = open_form(self.root, "Add Operator", [
            ("system_group_id", "System group ID", int),
            ("username", "Username", str),
            ("role", "Role (DISPATCHER / SUPERVISOR / ADMIN)", str),
            ("active", "Active (Y / N)", str)
        ])
        if operator is None:
            return

        try:
            operators.add_operator(
                operator[0], self.person_modul.selected,
                operator[1], operator[2], operator[3]
            )
        except Exception as exc:
            messagebox.showerror("Database error", str(exc))

    def edit(self, tree):
        if not self.selected:
            return

        vals = tree.item(self.selected, "values")

        operator = open_form(self.root, "Edit Operator Info", [
            ("operator_id", "Operator ID (read-only ID)", int),
            ("system_group_id", "System group ID", int),
            ("personal_id_number", "Personal identification number", str),
            ("username", "Username", str),
            ("role", "Role (DISPATCHER / SUPERVISOR / ADMIN)", str),
            ("active", "Active (Y / N)", str)
        ], {
            "operator_id": vals[0],
            "system_group_id": vals[1],
            "personal_id_number": vals[2],
            "username": vals[3],
            "role": vals[4],
            "active": vals[5]
        })
        if operator is None:
            return

        try:
            operators.update_operator(
                self.selected, operator[1], operator[2],
                operator[3], operator[4], operator[5]
            )
            tree.item(self.selected, values=operator)
        except Exception as exc:
            messagebox.showerror("Database error", str(exc))

    def delete(self):
        if not self.selected:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this operator?"
        ):
            return

        try:
            operators.delete_operator(self.selected)
        except Exception as exc:
            messagebox.showerror("Database error", str(exc))

        self.selected = None

    def load(self):
        return operators.list_operators()
