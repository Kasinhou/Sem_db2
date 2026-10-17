from ui.modules.module import Module
from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

class Attachment_module(Module):
    def __init__(self, root, case_file_module):
        super().__init__(root)
        self.case_file_module = case_file_module
        #entity_id = case_id ?
        self.des = ["attachment_id", "entity_type", "entity_id", "attachment_type", "file_content", "uploaded_by"]
        self.bigest_attachment_id = 0
    
    def add(self):
        if self.case_file_module.selected is None:
            return
    
        attachment = open_form(self.root,"Add Attachment", [
            ("entity_type", "Entity type", str),
            ("attachment_type", "Attachment type", str),
            ("file_content", "File content", "file")
        ])
        if(attachment is None):
            return
        #use sql
        self.bigest_attachment_id += 1
        self.values.append((self.bigest_attachment_id, attachment[0], self.case_file_module.selected[0], *attachment[1:], self.case_file_module.selected[1]))
    
    def edit(self,tree):
        if self.selected is None:
            return
    
        vals = tree.item(self.selected, "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        attachment = open_form(self.root,"Edit Attachment", [
            ("entity_type", "Entity type", str),
            ("attachment_type", "Attachment type", str),
            ("file_content", "File content", "file")
        ], {
            "entity_type": vals[1],
            "attachment_type": vals[3],
            "file_content": vals[4]
        })
        if(attachment is None):
            return
    
        tree.item(self.selected, values=(self.selected, attachment[0], vals[2], *attachment[1:], vals[5]))  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = (self.selected, attachment[0], vals[2], *attachment[1:], vals[5])
                break
        #use sql to save operator      
    
    def delete(self):
        if self.selected is None:
            return
    
        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this Attachment?"
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
                if value[2] == self.case_file_module.selected[0]:
                    res.append(value)
        return res