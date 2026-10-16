from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from ui.modules.system_group_module import System_group_module

class Unit_type_module:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root):
        if getattr(self, "_initialized", False):
            return
        self.selected_unit_type = None
        self.unit_types = [(0, "A56", "hasici")]
        self.bigest_unit_type_id = 0

        self.syste_group_module = System_group_module(root)

        self.des = ["unit_type_id", "code", "name"]  
        self._initialized = True
        self.root = root
    
    def edit_unit_type(self, tree):
        if self.selected_unit_type is None:
            return

        values = tree.item(self.selected_unit_type, "values")
        unit_type = open_form(self.root,"Edit Unit type Info", [
            ("code", "Code", str),
            ("name", "Name", str)
        ], {
            "code": values[1],
            "name": values[2]
        })
        if(unit_type is None):
            return

        tree.item(self.selected_unit_type, values=(self.selected_unit_type, *unit_type))  
        for i in range(len(self.unit_types)):
            if self.unit_types[i][0] == self.selected_unit_type:
                self.unit_types[i] = (self.selected_unit_type, *unit_type)  
                break
        #use sql to save operator        

    def delete_unit_type(self):
        if self.selected_unit_type is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this unit type?"
        ):
            return

        #ADD SQL
        for i in range(len(self.unit_types)):
            if self.unit_types[i][0] == self.selected_unit_type:
                self.unit_types.remove(self.unit_types[i])
                break
        
        self.selected_unit_type = None   

    def add_unit_type(self):
    
        unit_type = open_form(self.root,"Add Unit Type", [
            ("code", "Code", str),
            ("name", "Name", str)
        ])
        if(unit_type is None):
            return
        #use sql
        self.bigest_unit_type_id += 1
        self.unit_types.append((self.bigest_unit_type_id ,*unit_type))

    def load_data(self):
        #sql
        return self.unit_types