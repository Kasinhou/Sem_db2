from ui.modules.module import Module
from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime

class Case_note_module(Module):
    def __init__(self, root, case_file_module):
        super().__init__(root)
        self.case_file_module = case_file_module
        self.des = ["note_id", "case_id", "operator_id", "note_text", "created_at"]
        self.bigest_attachment_id = 0
    
    def add(self):
        if self.case_file_module.selected is None:
            return
    
        note = open_form(self.root,"Add Note", [
            ("note_text", "Note text", str),
            ("created_at", "Created at", datetime)
        ])
        if(note is None):
            return
        #use sql
        self.bigest_attachment_id += 1
        self.values.append((self.bigest_attachment_id, *self.case_file_module.selected, *note))
    
    def edit(self,tree):
        if self.selected is None:
            return
    
        vals = tree.item(self.selected, "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        attachment = open_form(self.root,"Edit Note", [
            ("note_text", "Note text", str),
            ("created_at", "Created at", datetime)
        ], {
            "note_text": vals[3],
            "created_at": vals[4]
        })
        if(attachment is None):
            return
    
        tree.item(self.selected, values=(self.selected, vals[1], vals[2], *attachment))  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = (self.selected, vals[1], vals[2], *attachment)
                break
        #use sql to save operator      
    
    def delete(self):
        if self.selected is None:
            return
    
        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this Note?"
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