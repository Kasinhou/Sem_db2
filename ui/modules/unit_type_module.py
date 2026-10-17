from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

from ui.modules.module import Module

class Unit_type_module(Module):

    def __init__(self, root, group_module):
        super().__init__(root)
        self.values = [(0, "A56", "hasici")]
        self.bigest_unit_type_id = 0

        self.syste_group_module = group_module

        self.des = ["unit_type_id", "code", "name"]  
    
    def edit(self, tree):
        if self.selected is None:
            return

        vals = tree.item(self.selected, "values")
        unit_type = open_form(self.root,"Edit Unit type Info", [
            ("code", "Code", str),
            ("name", "Name", str)
        ], {
            "code": vals[1],
            "name": vals[2]
        })
        if(unit_type is None):
            return

        tree.item(self.selected, values=(self.selected, *unit_type))  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = (self.selected, *unit_type)  
                break
        #use sql to save operator        

    def delete(self):
        if self.selected is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this unit type?"
        ):
            return

        #ADD SQL
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values.remove(self.values[i])
                break
        
        self.selected = None   

    def add(self):
    
        unit_type = open_form(self.root,"Add Unit Type", [
            ("code", "Code", str),
            ("name", "Name", str)
        ])
        if(unit_type is None):
            return
        #use sql
        self.bigest_unit_type_id += 1
        self.values.append((self.bigest_unit_type_id ,*unit_type))

    def load(self):
        #sql
        return self.values