from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

class Person_modul:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root):
        if getattr(self, "_initialized", False):
            return
        self.selected_operator = None
        self.people = [("841106/3456","Jozko","Mrkvicka"),("855130/3695","Magdalena","Mrkvova"),("850130/3695","Mojmir","Kovac"),("845312/7845","Marisa","Clnkova")] # temp data
        self.des = ["personal_id_number", "first_name", "last_name"]  
        self._initialized = True
        self.root = root

    def add_person(self):
        person = open_form(self.root,"Add Personal Info", [
            ("personal_id_number", "Personal identification number", str),
            ("first_name", "First name", str),
            ("last_name", "Last name", str)
        ])
 
        if(person is None):
            return

        #use sql to save person

        self.people.append(person)
    def edit_person(self,tree):
        if not self.selected_person:
            return

        values = tree.item(self.selected_person, "values")

        person = open_form(self.root,"Edit Personal Info", [
            ("original_personal_id_number", "Personal identification number (read-only ID)", str),
            ("first_name", "First name", str),
            ("last_name", "Last name", str)
        ], {
            "original_personal_id_number": values[0],
            "first_name": values[1],
            "last_name": values[2]
        })
        if(person is None):
            return

        tree.item(self.selected_person, values=person)  
        for i in range(len(self.people)):
            if self.people[i][0] == self.selected_person:
                self.people[i] = person 
                break
        #use sql to save person   

    def delete_person(self):
        if not self.selected_person:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this person?"
        ):
            return

        #ADD SQL
        for i in range(len(self.people)):
            if self.people[i][0] == self.selected_person:
                self.people.remove(self.people[i])
                break

        self.selected_person = None        

    def load_data(self):
        #sql
        return self.people