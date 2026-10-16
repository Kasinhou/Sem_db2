from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from ui.modules.system_group_module import System_group_module

class Unit_module:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root):
        if getattr(self, "_initialized", False):
            return
        self.selected_unit = None
        self.units = [(0,0,0,"CAS 30","available","gps_object","equipment_collection","path_to_photo")]
        self.bigest_unit_id = 0

        self.syste_group_module = System_group_module(root)

        self.des = ["unit_id", "unit_type_id", "system_group_id", "call_sign", "status", "last_position", "equipment", "photo"]  
        self._initialized = True
        self.root = root

    def add_unit(self):
        if self.syste_group_module.selected_system_group is None:
            return

        unit = open_form(self.root,"Add Unit", [
            ("unit_type_id", "Unit Type ID", int),
            ("call_sign", "Call Sign", str),
            ("status", "Status", str),
            ("last_position", "Last Postion", str),
            ("equipment", "Equipment", str),
            ("photo", "Phooto", "file")
        ])
        if(unit is None):
            return
        #use sql
        self.bigest_unit_id += 1
        self.units.append((self.bigest_unit_id, unit[0], self.syste_group_module.selected_system_group, *unit[1:]))

    
    def edit_unit(self, tree):
        if self.selected_unit is None:
            return

        values = tree.item(self.selected_unit, "values")

        unit = open_form(self.root,"Edit Unit Info", [
            ("unit_type_id", "Unit Type ID", int),
            ("system_group_id", "System group ID", int),
            ("call_sign", "Call Sign", str),
            ("status", "Status", str),
            ("last_position", "Last Postion", str),
            ("equipment", "Equipment", str),
            ("photo", "Photo", "file")
        ], {
            "unit_type_id": values[1],
            "system_group_id": values[2],
            "call_sign": values[3],
            "status": values[4],
            "last_position": values[5],
            "equipment": values[6],
            "photo": values[7],
        })
        if(unit is None):
            return

        tree.item(self.selected_unit, values=(self.selected_unit, *unit) )  
        for i in range(len(self.units)):
            if self.units[i][0] == self.selected_unit:
                self.units[i] = (self.selected_unit, *unit) 
                break
        #use sql to save contact     

    def delete_unit(self):
        if self.selected_unit is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this unit?"
        ):
            return

        #ADD SQL
        for i in range(len(self.units)):
            if self.units[i][0] == self.selected_unit:
                self.units.remove(self.units[i])
                break
        
        self.selected_unit = None

    def load_data(self):
        #sql
        return self.units