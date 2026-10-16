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
        if not self.operator_module.selected:
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
        print("NOT IMPLEMENTED YET")
    
    def delete(self):
        print("NOT IMPLEMENTED YET")
    
    def load(self):
        #add sql
        return self.values