from ui.reusable_ui_elements import open_form
import tkinter as tk
from tkinter import ttk, messagebox
from ui.modules.person_module import Person_modul

class Contact_module:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, root): 
        if getattr(self, "_initialized", False):
            return
        self.selected_contact = None
        self.bigest_contact_id = 0
        self.des = ["contact_id", "phone_number", "personal_id_number"]  
        self.person_modul = Person_modul(root)
        self.root = root
        self.contacts = [(0,"090315676","841106/3456")]
        self._initialized = True

    def edit_contact(self,tree):
        if self.selected_contact is None:
            return

        values = tree.item(self.selected_contact, "values")

        contact = open_form(self.root,"Edit Contact Info", [
            ("contact id", "Contact id (read-only ID)", int),
            ("phone number", "Phone number", str),
            ("original_personal_id_number", "Personal identification number", str)
        ], {
            "contact id": values[0],
            "phone number": values[1],
            "original_personal_id_number": values[2]
        })
        if(contact is None):
            return

        tree.item(self.selected_contact, values=contact)  
        for i in range(len(self.contacts)):
            if self.contacts[i][0] == self.selected_contact:
                self.contacts[i] = contact 
                break
        #use sql to save contact      
    def delete_contact(self):
        if self.selected_contact is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this contact?"
        ):
            return

        #ADD SQL
        for i in range(len(self.contacts)):
            if self.contacts[i][0] == self.selected_contact:
                self.contacts.remove(self.contacts[i])
                break
        
        self.selected_contact = None  
    
    def load_data(self):
        #sql
        return self.contacts

    def add_contact(self):
        if not self.person_modul.selected_person:
            return

        contact = open_form(self.root,"Add Contact", [
            ("phone_number", "Phone number", str)
        ])
        if(contact is None):
            return
        #use sql
        self.bigest_contact_id+=1
        self.contacts.append((self.bigest_contact_id,contact[0],self.person_modul.selected_person))