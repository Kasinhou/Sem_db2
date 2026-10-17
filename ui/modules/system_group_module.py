from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

from ui.modules.module import Module

class System_group_module(Module):

    def __init__(self, root):
        super().__init__(root)
        self.values = [(0, None, "Blavacky Hasici", "Bratislava")]
        self.bigest_system_group_id = 0

        self.des = ["system_group_id", "parent_group_id", "name", "region"]    

    def add(self):
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

        self.values.append(group)

    
    def edit(self, tree):
        if self.selected is None:
            return

        vals = tree.item(self.selected, "values")

        group = open_form(self.root,"Edit System group", [
            ("parent_group_id", "Parent group id", int),
            ("name", "Name", str),
            ("region", "Region", str)
        ], {
            "parent_group_id": vals[1],
            "name": vals[2],
            "region": vals[3]
        })
        if(group is None):
            return

        tree.item(self.selected, values=(int(vals[0]), *group))  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = (int(vals[0]), *group) 
                break
        #use sql to save person        

    def delete(self):
        if self.selected is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this group?"
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