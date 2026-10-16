from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime
from ui.modules.person_module import Person_modul

class Operator_modul:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root):
        if getattr(self, "_initialized", False):
            return
        self.selected_operator = None
        self.bigest_operator_id = 0
        self.des = ["operator_id","system_group_id","username","role","hire_date","personal_id_number"]  
        self.person_modul = Person_modul(root)
        self.root = root
        self.operators = [(0,0,"Magda","someone",datetime.now(),"855130/3695")]
        self._initialized = True

    def edit_operator(self, tree):
        if self.selected_operator is None:
            return

        values = tree.item(self.selected_operator, "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        operator = open_form(self.root,"Edit Operator Info", [
            ("operator_id", "Operator ID (read-only ID)", int),
            ("system_group_id", "System group id name", int),
            ("username", "Username", str),
            ("role", "Role", str),
            ("hire date", "Hire date", date),
            ("personal id number", "Personal identification number", str)
        ], {
            "operator_id": values[0],
            "system_group_id": values[1],
            "username": values[2],
            "role": values[3],
            "hire date": values[4],
            "personal id number": values[5]
        })
        if(operator is None):
            return

        tree.item(self.selected_operator, values=operator)  
        for i in range(len(self.operators)):
            if self.operators[i][0] == self.selected_operator:
                self.operators[i] = operator 
                break
        #use sql to save operator       
    def delete_operator(self):
        if self.selected_operator is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this operator?"
        ):
            return

        #ADD SQL
        for i in range(len(self.operators)):
            if self.operators[i][0] == self.selected_operator:
                self.operators.remove(self.operators[i])
                break
        
        self.selected_operator = None    
    
    def load_data(self):
        #sql
        return self.operators

    def add_operator(self):
        if not self.person_modul.selected_person:
            return

        operator = open_form(self.root,"Add Operator", [
            ("system_group_id", "System group ID", int),
            ("username", "Username", str),
            ("role", "Role", str),
            ("hire_date", "Hire date (YYYY-MM-DD)", date)
        ])
        if(operator is None):
            return
        #use sql
        self.bigest_operator_id += 1
        self.operators.append((self.bigest_operator_id,operator[0],operator[1],operator[2],operator[3],self.person_modul.selected_person))