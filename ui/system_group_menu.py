import tkinter as tk
from tkinter import ttk, messagebox
from ui.reusable_ui_elements import setup_table, open_form, update_table_columns
from datetime import date, datetime

class System_group_menu:
    def __init__(self, root, group_module, unit_module, unit_type_module):
        self.root = root
        self.current_view = 0 #0 - system_groups, 1 - units, 2 - unit_types;
        
        self.system_group_module = group_module
        self.unit_module = unit_module
        self.unit_type_module = unit_type_module

        self.modules = [self.system_group_modul, self.unit_module, self.unit_type_module]
       
        self.create()


    def create(self):
        header = ttk.Frame(self.root, padding=15)
        header.pack(fill="x")

        ttk.Label(
            header,
            text="System group Manager",
            font=("Arial", 18, "bold")
        ).pack(anchor="w")

        # Main actions
        top_buttons = ttk.Frame(self.root, padding=(15, 0, 15, 15))
        top_buttons.pack(fill="x")

        ttk.Button(
            top_buttons,
            text="Add System group",
            command=lambda: (
                self.system_group_module.add(),
                self.load_data()
            )
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Add Unit Type",
            command=lambda: (
                self.unit_type_module.add(),
                setattr(self, "current_view", 2),
                self.update_view_table()
            )
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Get System groups",
            command= lambda: (setattr(self, "current_view", 0), self.update_view_table())
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Get Units",
            command=lambda: (setattr(self, "current_view", 1), self.update_view_table())
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Get Unit_types",
            command=lambda: (setattr(self, "current_view", 2), self.update_view_table())
        ).pack(side="left")

        self.action_buttons = []
        # Table
        self.tree = setup_table(self.root,["system_group_id", "parent_group_id", "name", "region"])
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

        buttons = [
            ("Edit", self.edit_data),
            ("Delete", self.delete_data),
            ("Add Unit", lambda: (
                    self.unit_module.add(),
                    setattr(self, "current_view", 1),
                    self.update_view_table()
                )
            ),
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
               
        for row in self.modules[self.current_view].load():
            self.tree.insert("", "end", iid=row[0], values=row)
        
        for module in self.modules:
            module.selected = None
        for button in self.action_buttons:
            button.config(state="disabled")


    def on_selected(self, event=None):
        selected = self.tree.selection()

        if selected:
            match self.current_view:
                case 0:
                    self.system_group_module.selected = int(selected[0])
                    for button in self.action_buttons:
                        button.config(state="normal")
                case 1:
                    self.unit_module.selected = int(selected[0])                
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
                case 2:
                    self.unit_type_module.selected = int(selected[0])               
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
        else:
            for module in self.modules:
                module.selected = None

            for button in self.action_buttons:
                button.config(state="disabled")
   
    
    def update_view_table(self):
        update_table_columns(self.tree, self.modules[self.current_view].des)
        self.load_data()    

    def edit_data(self):
        self.modules[self.current_view].edit(self.tree)

    def delete_data(self):        
        self.modules[self.current_view].delete()
        self.load_data()
        

