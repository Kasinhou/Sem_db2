from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

from ui.modules.module import Module

class Operator_modul(Module):

    def __init__(self, root, person_module):
        super().__init__(root)
        self.bigest_operator_id = 0
        self.des = ["operator_id","system_group_id","username","role","hire_date","personal_id_number"]  
        self.person_modul = person_module
        self.values = [(0,0,"Magda","someone",datetime.now(),"855130/3695")]

    def edit(self, tree):
        if self.selected is None:
            return

        vals = tree.item(self.selected, "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        operator = open_form(self.root,"Edit Operator Info", [
            ("operator_id", "Operator ID (read-only ID)", int),
            ("system_group_id", "System group id name", int),
            ("username", "Username", str),
            ("role", "Role", str),
            ("hire date", "Hire date", date),
            ("personal id number", "Personal identification number", str)
        ], {
            "operator_id": vals[0],
            "system_group_id": vals[1],
            "username": vals[2],
            "role": vals[3],
            "hire date": vals[4],
            "personal id number": vals[5]
        })
        if(operator is None):
            return

        tree.item(self.selected, values=operator)  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = operator 
                break
        #use sql to save operator       
    def delete(self):
        if self.selected is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this operator?"
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

    def add(self):
        if not self.person_modul.selected:
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
        self.values.append((self.bigest_operator_id,operator[0],operator[1],operator[2],operator[3],self.person_modul.selected))