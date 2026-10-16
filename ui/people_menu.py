import tkinter as tk
from tkinter import ttk, messagebox
from ui.reusable_ui_elements import setup_table, open_form, update_table_columns
from datetime import date, datetime
from ui.modules.person_module import Person_modul
from ui.modules.operator_module import Operator_modul
from ui.modules.contact_module import Contact_module

class People_menu:
    def __init__(self, root):
        self.root = root
        self.current_view = 0 #0 - people, 1 - contacts, 2 - operators;

        self.person_module = Person_modul(root)
        self.operator_module = Operator_modul(root)
        self.contact_module = Contact_module(root)
        
        self.create()


    def create(self):
        header = ttk.Frame(self.root, padding=15)
        header.pack(fill="x")

        ttk.Label(
            header,
            text="Personal Information Manager",
            font=("Arial", 18, "bold")
        ).pack(anchor="w")

        # Main actions
        top_buttons = ttk.Frame(self.root, padding=(15, 0, 15, 15))
        top_buttons.pack(fill="x")

        ttk.Button(
            top_buttons,
            text="Add Personal Info",
            command=lambda: (
                self.person_module.add_person(),
                self.load_data()
            )
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Get Personal Infos",
            command= lambda: (setattr(self, "current_view", 0), self.update_view_table())
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Get Contact Infos",
            command=lambda: (setattr(self, "current_view", 1), self.update_view_table())
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Get Operator Infos",
            command=lambda: (setattr(self, "current_view", 2), self.update_view_table())
        ).pack(side="left")

        self.action_buttons = []
        # Table
        self.tree = setup_table(self.root,["personal_id_number", "first_name", "last_name"])
        self.load_data()
        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_selected
        )

        # Actions for the selected person
        actions = ttk.LabelFrame(
            self.root,
            text="Selected data Actions",
            padding=10
        )
        actions.pack(fill="x", padx=15, pady=15)

        #self.action_buttons = []

        buttons = [
            ("Edit", self.edit_data),
            ("Delete", self.delete_data),
            ("Add Contact", lambda: (
                    self.contact_module.add_contact(),
                    setattr(self, "current_view", 1),
                    self.update_view_table()
                )
            ),
            ("Add Operator", lambda: (
                    self.operator_module.add_operator(),
                    setattr(self, "current_view", 2),
                    self.update_view_table()
                )
            )
        ]

        for text, command in buttons:
            button = ttk.Button(
                actions,
                text=text,
                command=command,
                state="disabled"
            )
            button.pack(side="left", padx=5)
            self.action_buttons.append(button)
        

    def load_data(self):        
        self.tree.delete(*self.tree.get_children())

        match self.current_view:
            case 0:
                for row in self.person_module.load_data():
                    self.tree.insert("", "end", iid=row[0], values=row)
            case 1:
                for row in self.contact_module.load_data():
                    self.tree.insert("", "end", iid=row[0], values=row)
            case 2:
                for row in self.operator_module.load_data():
                    self.tree.insert("", "end", iid=row[0], values=row)

        self.person_module.selected_person = None
        self.contact_module.selected_contact = None
        self.operator_module.selected_operator = None
        for button in self.action_buttons:
            button.config(state="disabled")


    def on_selected(self, event=None):
        selected = self.tree.selection()

        if selected:
            match self.current_view:
                case 0:
                    self.person_module.selected_person = selected[0]
                    for button in self.action_buttons:
                        button.config(state="normal")
                case 1:
                    self.contact_module.selected_contact = int(selected[0])                
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
                case 2:
                    self.operator_module.selected_operator = int(selected[0])               
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
        else:
            self.person_module.selected_person = None
            self.contact_module.selected_contact = None
            self.operator_module.selected_operator = None

            for button in self.action_buttons:
                button.config(state="disabled")
    
    
    def update_view_table(self):
        match self.current_view:
            case 0:                      
                update_table_columns(self.tree, self.person_module.des)
            case 1:      
                update_table_columns(self.tree,  self.contact_module.des)
            case 2:                      
                update_table_columns(self.tree, self.operator_module.des)
        self.load_data()


    def edit_data(self):
        match self.current_view:
            case 0:
                self.person_module.edit_person(self.tree)
            case 1:
                self.contact_module.edit_contact(self.tree)
            case 2:
                self.operator_module.edit_operator(self.tree)

    def delete_data(self):
        match self.current_view:
            case 0:
                self.person_module.delete_person()
            case 1:
                self.contact_module.delete_contact()
            case 2:
                self.operator_module.delete_operator()
        self.load_data()
        

