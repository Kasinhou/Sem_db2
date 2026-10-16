from ui.modules.module import Module
from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

class Call_report_module(Module):
    def __init__(self, root, operator_module):
        super().__init__(root)
        self.operator_module = operator_module
        self.des = ["call_id", "contact_id", "operator_id", "case_id", "call_datetime", "duration_seconds", "status"]
        self.bigest_call_id = 0

    def add(self):
        if self.operator_module.selected is None:
            return

        record = open_form(self.root,"Add Call Record", [
            ("contact_id", "Contact ID", int),
            ("case_id", "Case ID", int),
            ("call_datetime", "Call Datetime", datetime),
            ("duration_seconds", "Duration seconds", int),
            ("status", "Status", str)
        ])
        if(record is None):
            return
        #use sql
        self.bigest_call_id += 1
        self.values.append((self.bigest_call_id, record[0], self.operator_module.selected, *record[1:]))
    
    def edit(self,tree):
        if self.selected is None:
            return

        vals = tree.item(self.selected, "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        record = open_form(self.root,"Edit Operator Info", [
            ("contact_id", "Contact ID", int),
            ("case_id", "Case ID", int),
            ("call_datetime", "Call Datetime", datetime),
            ("duration_seconds", "Duration seconds", int),
            ("status", "Status", str)
        ], {
            "contact_id": vals[1],
            "case_id": vals[3],
            "call_datetime": vals[4],
            "duration_seconds": vals[5],
            "status": vals[6]
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
            "Do you really want to delete this call record?"
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
        return self.values