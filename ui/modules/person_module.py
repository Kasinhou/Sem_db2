from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

from ui.modules.module import Module

class Person_modul(Module):

    def __init__(self, root):
        super().__init__(root)
        self.values = [("841106/3456","Jozko","Mrkvicka"),("855130/3695","Magdalena","Mrkvova"),("850130/3695","Mojmir","Kovac"),("845312/7845","Marisa","Clnkova")] # temp data
        self.des = ["personal_id_number", "first_name", "last_name"]  

    def add(self):
        person = open_form(self.root,"Add Personal Info", [
            ("personal_id_number", "Personal identification number", str),
            ("first_name", "First name", str),
            ("last_name", "Last name", str)
        ])
 
        if(person is None):
            return

        #use sql to save person

        self.values.append(person)
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

        tree.item(self.selected, values=person)  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = person 
                break
        #use sql to save person   

    def delete(self):
        if not self.selected:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this person?"
        ):
            return

        #ADD SQL
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values.remove(self.values[i])
                break

        self.selected = None        

    def load(self):
        #sql
        return self.values