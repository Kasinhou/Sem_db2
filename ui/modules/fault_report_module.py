from ui.modules.module import Module
from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

class Fault_report_module(Module):
    def __init__(self, root, operator_module):
        super().__init__(root)
        self.operator_module = operator_module
        self.des = ["fault_id", "unit_id", "reported_by", "status", "reported_at", "resolved_at"]
        self.bigest_fault_id = 0
    
    def add(self):
        if self.operator_module.selected is None:
            return
    
        record = open_form(self.root,"Add Fault Report", [
            ("unit_id", "Unit ID", int),
            ("status", "Status", str),
            ("reported_at", "Reported at", datetime),
            ("resolved_at", "Resolved at", datetime)
        ])
        if(record is None):
            return
        #use sql
        self.bigest_fault_id += 1
        self.values.append((self.bigest_fault_id, record[0], self.operator_module.selected, *record[1:]))
    
    def edit(self,tree):
        if self.selected is None:
            return
    
        vals = tree.item(self.selected, "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        record = open_form(self.root,"Edit Fault report", [
            ("unit_id", "Unit ID", int),
            ("status", "Status", str),
            ("reported_at", "Reported at", datetime),
            ("resolved_at", "Resolved at", datetime)
        ], {
            "unit_id": vals[1],
            "status": vals[3],
            "reported_at": vals[4],
            "resolved_at": vals[5]
        })
        if(record is None):
            return
    
        tree.item(self.selected, values=(self.selected, record[0], vals[2], *record[1:]))  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = (self.selected, record[0], vals[2], *record[1:])
                break
        #use sql to save operator      
    
    def delete(self):
        if self.selected is None:
            return
    
        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this fault report?"
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

        if self.operator_module.selected is None:
            return res
        else:
            for value in self.values:
                if value[2] == self.operator_module.selected:
                    res.append(value)
        return res