from ui.modules.module import Module
from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

class Case_unit_assignment_module(Module):
    def __init__(self, root, case_file_module):
        super().__init__(root)
        self.case_file_module = case_file_module
        self.des = ["assignment_id", "case_id", "unit_id", "dispatched_at", "arrived_at"]
        self.bigest_assignment_id = 0
    
    def add(self):
        if self.case_file_module.selected is None:
            return
    
        case_file = open_form(self.root,"Add Case Unit assignment", [
            ("unit_id", "Unit ID", int),
            ("dispatched_at", "Dispatched at", datetime),
            ("arrived_at", "Arrived at", datetime)
        ])
        if(case_file is None):
            return
        #use sql
        self.bigest_assignment_id += 1
        self.values.append((self.bigest_assignment_id, self.case_file_module.selected[0], *case_file))
    
    def edit(self,tree):
        if self.selected is None:
            return
    
        vals = tree.item(self.selected, "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        case_file = open_form(self.root,"Edit Case Unit assignment", [
            ("unit_id", "Unit ID", int),
            ("dispatched_at", "Dispatched at", datetime),
            ("arrived_at", "Arrived at", datetime)
        ], {
            "unit_id": vals[2],
            "dispatched_at": vals[3],
            "arrived_at": vals[4]
        })
        if(case_file is None):
            return
    
        tree.item(self.selected, values=(self.selected, vals[1], *case_file))  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = (self.selected, vals[1], *case_file)
                break
        #use sql to save operator      
    
    def delete(self):
        if self.selected is None:
            return
    
        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this case unit assignment?"
        ):
            return
    
        #ADD SQL
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values.remove(self.values[i])
                break
    
        self.selected = None    
    
    def load(self):
        #add sql
        res = []

        if self.case_file_module.selected is None:
            return res
        else:
            for value in self.values:
                if value[1] == self.case_file_module.selected[0]:
                    res.append(value)
        return res