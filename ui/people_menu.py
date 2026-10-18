import tkinter as tk
from datetime import date, datetime
from tkinter import ttk, messagebox

from ui.reusable_ui_elements import setup_table, update_table_columns


class People_menu:
    def __init__(self, root, person_module, operator_module, contact_module):
        self.root = root
        self.current_view = 0  # 0 - people, 1 - contacts, 2 - operators;

        # style
        style = ttk.Style()
        style.map("TButton",
                  foreground=[
                      ("disabled", "#888888"),
                  ],
                  background=[
                      ("disabled", "#C7C7C7"),
                      ("pressed", "#003366"),
                  ]
                  )

        self.person_module = person_module
        self.operator_module = operator_module
        self.contact_module = contact_module

        self.modules = [self.person_module, self.contact_module, self.operator_module]

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
                self.person_module.add(),
                self.load_data()
            )
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Get Personal Infos",
            command=lambda: (setattr(self, "current_view", 0), self.update_view_table())
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
        self.tree = setup_table(self.root, ["personal_id_number", "first_name", "last_name"])
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
                    self.contact_module.add(),
                    setattr(self, "current_view", 1),
                    self.update_view_table()
                )
            ),
            ("Add Operator", lambda: (
                    self.operator_module.add(),
                    setattr(self, "current_view", 2),
                    self.update_view_table()
                )
            ),
            ("Get Age", lambda: self.person_module.show_age()),
            ("Get Sex", lambda: self.person_module.show_sex()),
            ("Show XML", self.operator_module.show_xml),
            ("Export XML", self.operator_module.export_xml)
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

        self.update_ui_state()

    def load_data(self):
        self.tree.delete(*self.tree.get_children())

        for row in self.modules[self.current_view].load():
            self.tree.insert("", "end", iid=row[0], values=row)

        for module in self.modules:
            module.selected = None
        for button in self.action_buttons:
            button.config(state="disabled")

    # Manages the visibility and state of all dynamic buttons based on current_view
    def update_ui_state(self):
        # Edit (0), Delete (1) always
        for i in (0, 1):
            self.action_buttons[i].pack(side="left", padx=5)

        # Add Contact (2), Add Operator (3), Get Age(4), Get Sex(5)  visible only in Personal Info (0)
        for i in (2, 3, 4, 5):
            if self.current_view == 0:
                self.action_buttons[i].pack(side="left", padx=5)
            else:
                self.action_buttons[i].pack_forget()

        # Show XML (6), Export XML (7) visible only in Operators (2)
        for i in (6, 7):
            if self.current_view == 2:
                self.action_buttons[i].pack(side="left", padx=5)
            else:
                self.action_buttons[i].pack_forget()

    def on_selected(self, event=None):
        selected = self.tree.selection()

        if selected:
            match self.current_view:
                # Personal Info
                case 0:
                    self.person_module.selected = selected[0]
                    for i in range(6):
                        self.action_buttons[i].config(state="normal")
                    for i in (6, 7):
                        self.action_buttons[i].config(state="disabled")

                # Contacts
                case 1:
                    self.contact_module.selected = int(selected[0])
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
                    for i in range(2, 8):
                        self.action_buttons[i].config(state="disabled")

                # Operators
                case 2:
                    self.operator_module.selected = int(selected[0])
                    for i in (0, 1, 6, 7):
                        self.action_buttons[i].config(state="normal")
                    for i in (2, 3, 4, 5):
                        self.action_buttons[i].config(state="disabled")
        else:
            for module in self.modules:
                module.selected = None

            for button in self.action_buttons:
                button.config(state="disabled")

    def update_view_table(self):
        update_table_columns(self.tree, self.modules[self.current_view].des)
        self.load_data()
        self.update_ui_state()

    def edit_data(self):
        self.modules[self.current_view].edit(self.tree)

    def delete_data(self):
        self.modules[self.current_view].delete()
        self.load_data()
