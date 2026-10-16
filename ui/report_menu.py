
import tkinter as tk
from tkinter import ttk, messagebox

from ui.reusable_ui_elements import setup_table, update_table_columns

class Report_menu:

    def __init__(self, root,
        operator_module,
        call_report_module,
        case_file_module,
        fault_report_module,
        case_unit_module,
        attachment_module,
        case_note_module):
        self.root = root

        self.operator_module = operator_module
        self.call_report_module = call_report_module
        self.fault_report_module = fault_report_module
        self.case_file_module = case_file_module
        self.case_unit_module = case_unit_module
        self.attachment_module = attachment_module
        self.case_note_module = case_note_module

        self.modules = [self.operator_module, self.call_report_module, self.fault_report_module, self.case_file_module, self.case_unit_module, self.attachment_module, self.case_note_module]

        self.current_view = 0 #0 - operators, 1-call reports, 2 - fault reports, 3 - case files, 4 - case unit assognments, 5 -attachments, 6 case notes

        self.create()

    def create(self):
        header = ttk.Frame(self.root, padding=15)
        header.pack(fill="x")

        ttk.Label(
            header,
            text="Report Manager",
            font=("Arial", 18, "bold")
        ).pack(anchor="w")

        # Main actions
        top_buttons = ttk.Frame(self.root, padding=(15, 0, 15, 15))
        top_buttons.pack(fill="x")

        self.action_buttons = []

        # VRCH: GET operators| GET/ADD Call Reports(av only if op selected) | GET/ADD Fault Reports(av only if op selected) | GET/ADD Case files(av only if op selected)
        ttk.Button(
            top_buttons,
            text="Get Operator Infos",
            command=lambda: (setattr(self, "current_view", 0), self.update_view_table())
        ).pack(side="left", padx=(0, 10))

        button = ttk.Button(
            top_buttons,
            text="Get Call Reports",
            command=lambda: (setattr(self, "current_view", 1), self.update_view_table())
        )
        button.pack(side="left", padx=(0, 10))
        button = ttk.Button(
            top_buttons,
            text="Add Call Report",
            command=lambda: (self.call_report_module.add() ,setattr(self, "current_view", 1), self.update_view_table())
        )
        button.pack(side="left", padx=(0, 10))
        self.action_buttons.append(button)        

        button = ttk.Button(
            top_buttons,
            text="Get Fault Reports",
            command=lambda: (setattr(self, "current_view", 2), self.update_view_table())
        )
        button.pack(side="left", padx=(0, 10))
        button = ttk.Button(
            top_buttons,
            text="Add Fault Report",
            command=lambda: (self.fault_report_module.add() ,setattr(self, "current_view", 2), self.update_view_table())
        )
        button.pack(side="left", padx=(0, 10))
        self.action_buttons.append(button)   
        
        button = ttk.Button(
            top_buttons,
            text="Get Case files",
            command=lambda: (setattr(self, "current_view", 3), self.update_view_table())
        )
        button.pack(side="left", padx=(0, 10))
        button = ttk.Button(
            top_buttons,
            text="Add Case file",
            command=lambda: (self.case_file_module.add() ,setattr(self, "current_view", 3), self.update_view_table())
        )
        button.pack(side="left", padx=(0, 10))
        self.action_buttons.append(button)    
        
        # Table
        self.tree = setup_table(self.root,self.operator_module.des)
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
            ("Add Case unit assignment", lambda: (
                    self.case_unit_module.add(),
                    setattr(self, "current_view", 4),
                    self.update_view_table()
                )
            ),
            ("Get Case unit assignment", lambda: (
                    setattr(self, "current_view", 4),
                    self.update_view_table()
                )
            ),
            ("Add Attachment", lambda: (
                    self.attachment_module.add(),
                    setattr(self, "current_view", 5),
                    self.update_view_table()
                )
            ),
            ("Get Attachment", lambda: (
                    setattr(self, "current_view", 5),
                    self.update_view_table()
                )
            ),
            ("Add Case note", lambda: (
                    self.case_note_module.add(),
                    setattr(self, "current_view", 6),
                    self.update_view_table()
                )
            ),
            ("Get Case note", lambda: (
                    setattr(self, "current_view", 6),
                    self.update_view_table()
                )
            )
        ] #14 buttons

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
            module.selected = False
        for button in self.action_buttons:
            button.config(state="disabled")


    def on_selected(self, event=None):
        selected = self.tree.selection()

        if selected:
            match self.current_view:
                case 0:
                    self.operator_module.selected = selected[0]
                    for i in range(8):
                        self.action_buttons[i].config(state="normal")
                case 1:
                    self.call_report_module.selected = selected[0]
                    for i in range(6,8):
                        self.action_buttons[i].config(state="normal")
                case 2:
                    self.fault_report_module.selected = selected[0]
                    for i in range(6,8):
                        self.action_buttons[i].config(state="normal")
                case 3:
                    self.case_file_module.selected = selected[0]
                    for i in range(6,14):
                        self.action_buttons[i].config(state="normal")
                case 4:
                    self.case_unit_module.selected = selected[0]
                    for i in range(6,8):
                        self.action_buttons[i].config(state="normal")
                case 5:
                    self.attachment_module.selected = selected[0]
                    for i in range(6,8):
                        self.action_buttons[i].config(state="normal")
                case 6:
                    self.case_note_module.selected = selected[0]
                    for i in range(6,8):
                        self.action_buttons[i].config(state="normal")
        else:
            for module in self.modules:
                module.selected = False
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
    