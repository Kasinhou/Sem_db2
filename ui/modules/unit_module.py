from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

from ui.modules.module import Module

class Unit_module(Module):

    def __init__(self, root, group_module):
        super().__init__(root)
        self.values = [(0,0,0,"CAS 30","available","gps_object","equipment_collection","path_to_photo")]
        self.bigest_unit_id = 0

        self.syste_group_module = group_module

        self.des = ["unit_id", "unit_type_id", "system_group_id", "call_sign", "status", "last_position", "equipment", "photo"]  

    def add(self):
        if self.syste_group_module.selected is None:
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
        self.values.append((self.bigest_unit_id, unit[0], self.syste_group_module.selected, *unit[1:]))

    
    def edit(self, tree):
        if self.selected is None:
            return

        vals = tree.item(self.selected, "values")

        unit = open_form(self.root,"Edit Unit Info", [
            ("unit_type_id", "Unit Type ID", int),
            ("system_group_id", "System group ID", int),
            ("call_sign", "Call Sign", str),
            ("status", "Status", str),
            ("last_position", "Last Postion", str),
            ("equipment", "Equipment", str),
            ("photo", "Photo", "file")
        ], {
            "unit_type_id": vals[1],
            "system_group_id": vals[2],
            "call_sign": vals[3],
            "status": vals[4],
            "last_position": vals[5],
            "equipment": vals[6],
            "photo": vals[7],
        })
        if(unit is None):
            return

        tree.item(self.selected, values=(self.selected, *unit) )  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = (self.selected, *unit) 
                break
        #use sql to save contact     

    def delete(self):
        if self.selected is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this unit?"
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