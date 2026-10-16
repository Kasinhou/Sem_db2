from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

class System_group_module:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root):
        if getattr(self, "_initialized", False):
            return
        self.selected_system_group = None
        self.system_groups = [(0, None, "Blavacky Hasici", "Bratislava")]
        self.bigest_system_group_id = 0

        self.des = ["system_group_id", "parent_group_id", "name", "region"]    
        self._initialized = True
        self.root = root

    def add_system_group(self):
        group = open_form(self.root,"Add System group", [
            ("parent_group_id", "Parent group id", int),
            ("name", "Name", str),
            ("region", "Region", str)
        ])

        if(group is None):
            return
        
        #use sql to save person

        self.bigest_system_group_id += 1
        group = (self.bigest_system_group_id , *group)

        self.system_groups.append(group)

    
    def edit_system_group(self, tree):
        if self.selected_system_group is None:
            return

        values = tree.item(self.selected_system_group, "values")

        group = open_form(self.root,"Edit System group", [
            ("parent_group_id", "Parent group id", int),
            ("name", "Name", str),
            ("region", "Region", str)
        ], {
            "parent_group_id": values[0],
            "name": values[1],
            "region": values[2]
        })
        if(group is None):
            return

        tree.item(self.selected_system_group, values=(values[0], *group))  
        for i in range(len(self.system_groups)):
            if self.system_groups[i][0] == self.selected_system_group:
                self.system_groups[i] = (values[0], *group) 
                break
        #use sql to save person        

    def delete_system_group(self):
        if self.selected_system_group is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this group?"
        ):
            return

        #ADD SQL
        for i in range(len(self.system_groups)):
            if self.system_groups[i][0] == self.selected_system_group:
                self.system_groups.remove(self.system_groups[i])
                break
        
        self.selected_system_group = None   

    def load_data(self):
        #sql
        return self.system_groups