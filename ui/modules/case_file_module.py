from ui.modules.module import Module
from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime


class Case_file_module(Module):
    def __init__(self, root, operator_module):
        super().__init__(root)
        self.operator_module = operator_module
        self.des = ["case_id", "created_by", "case_number", "opened_at", "closed_at", "status", "weather_snapshot"]
        self.bigest_case_id = 0
    
    def add(self):
        if self.operator_module.selected is None:
            return
    
        case_file = open_form(self.root,"Add Case file", [
            ("case_number", "Case number", str),
            ("opened_at", "Opened at", datetime),
            ("closed_at", "Closed at", datetime),
            ("status", "Status", str),
            ("weather_snapshot", "Wather snapshot", "file")
        ])
        if(case_file is None):
            return
        #use sql
        self.bigest_case_id += 1
        self.values.append((self.bigest_case_id, self.operator_module.selected, *case_file))
    
    def edit(self,tree):
        if self.selected is None:
            return
    
        vals = tree.item(self.selected[0], "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        case_file = open_form(self.root,"Edit Case file", [
            ("case_number", "Case number", str),
            ("opened_at", "Opened at", datetime),
            ("closed_at", "Closed at", datetime),
            ("status", "Status", str),
            ("weather_snapshot", "Wather snapshot", "file")
        ], {
            "case_number": vals[2],
            "opened_at": vals[3],
            "closed_at": vals[4],
            "status": vals[5],
            "weather_snapshot": vals[6]
        })
        if(case_file is None):
            return
    
        tree.item(self.selected[0], values=(self.selected[0], vals[1], *case_file))  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected[0]:
                self.values[i] = (self.selected[0], vals[1], *case_file)
                break
        #use sql to save operator      
    
    def delete(self):
        if self.selected is None:
            return
    
        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this case file?"
        ):
            return
    
        #ADD SQL
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected[0]:
                self.values.remove(self.values[i])
                break
    
        self.selected = None    
    
    def load(self):
        #add sql
        res = []

        if self.operator_module.selected is None:
            return res
        else:
            for value in self.values:
                if value[1] == self.operator_module.selected:
                    res.append(value)
        return res