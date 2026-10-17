from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox

from ui.modules.module import Module

class Contact_module(Module):
    def __init__(self, root, person_module): 
        super().__init__(root)
        self.selected = None
        self.bigest_contact_id = 0
        self.des = ["contact_id", "phone_number", "personal_id_number"]  
        self.person_modul = person_module
        self.values = [(0,"090315676","841106/3456")]

    def edit(self,tree):
        if self.selected is None:
            return

        vals = tree.item(self.selected, "values")

        contact = open_form(self.root,"Edit Contact Info", [
            ("contact id", "Contact id (read-only ID)", int),
            ("phone number", "Phone number", str),
            ("original_personal_id_number", "Personal identification number", str)
        ], {
            "contact id": vals[0],
            "phone number": vals[1],
            "original_personal_id_number": vals[2]
        })
        if(contact is None):
            return

        tree.item(self.selected, values=contact)  
        for i in range(len(self.values)):
            if self.values[i][0] == self.selected:
                self.values[i] = contact 
                break
        #use sql to save contact      
    def delete(self):
        if self.selected is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this contact?"
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

    def add(self):
        if not self.person_modul.selected:
            return

        contact = open_form(self.root,"Add Contact", [
            ("phone_number", "Phone number", str)
        ])
        if(contact is None):
            return
        #use sql
        self.bigest_contact_id+=1
        self.values.append((self.bigest_contact_id,contact[0],self.person_modul.selected))