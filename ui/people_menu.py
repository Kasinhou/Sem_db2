import tkinter as tk
from tkinter import ttk, messagebox
from ui.reusable_ui_elements import setup_table, open_form

class People_menu:
    def __init__(self, root):
        self.root = root
        self.selected_person = None
        self.create()
        self.temp_people = [("841106/3456","Jozko","Mrkvicka"),("855130/3695","Magdalena","Mrkvova"),("850130/3695","Mojmir","Kovac"),("845312/7845","Marisa","Clnkova")]


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
            command=self.add_person
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Get Personal Infos",
            command=self.load_people
        ).pack(side="left")

        # Table
        des = ["personal_id_number", "first_name", "last_name"]        
        self.tree = setup_table(self.root, des)
        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_person_selected
        )

        # Actions for the selected person
        actions = ttk.LabelFrame(
            self.root,
            text="Selected Person Actions",
            padding=10
        )
        actions.pack(fill="x", padx=15, pady=15)

        self.action_buttons = []

        buttons = [
            ("Edit", self.edit_person),
            ("Delete", self.delete_person),
            ("Add Contact", self.add_contact),
            ("Add Operator", self.add_operator),
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
    
    def add_person(self):
        person = open_form(self.root,"Add Personal Info", [
            ("personal_id_number", "Personal identification number"),
            ("first_name", "First name"),
            ("last_name", "Last name")
        ])

        if(person is None):
            return
        
        #use sql to save person

        self.temp_people.append(person)
        self.load_people()

    def edit_person(self):
        if not self.selected_person:
            return

        values = self.tree.item(self.selected_person, "values")

        person = open_form(self.root,"Edit Personal Info", [
            ("original_personal_id_number", "Personal identification number (read-only ID)"),
            ("first_name", "First name"),
            ("last_name", "Last name")
        ], {
            "original_personal_id_number": values[0],
            "first_name": values[1],
            "last_name": values[2]
        })
        if(person is None):
            return

        self.tree.item(self.selected_person, values=person)  
        for i in range(len(self.temp_people)):
            if self.temp_people[i][0] == self.selected_person:
                self.temp_people[i] = person 
                break
        #use sql to save person        
    
    def delete_person(self):
        if not self.selected_person:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this person?"
        ):
            return

        #ADD SQL
        for i in range(len(self.temp_people)):
            if self.temp_people[i][0] == self.selected_person:
                self.temp_people.remove(self.temp_people[i])
                break
        
        self.selected_person = None
        self.load_people()

    def load_people(self):
        #Write select here
        
        self.tree.delete(*self.tree.get_children())

        for row in self.temp_people:
            self.tree.insert("", "end", iid=row[0], values=row)

        self.selected_person = None
        for button in self.action_buttons:
            button.config(state="disabled")


    def on_person_selected(self, event=None):
        selected = self.tree.selection()

        if selected:
            self.selected_person = selected[0]

            for button in self.action_buttons:
                button.config(state="normal")
        else:
            self.selected_person = None

            for button in self.action_buttons:
                button.config(state="disabled")

    def add_contact(self):
        if not self.selected_person:
            return

        contact = open_form(self.root,"Add Contact", [
            ("phone_number", "Phone number")
        ])
        if(contact is None):
            return
        #use sql

    def add_operator(self):
        if not self.selected_person:
            return

        operator = open_form(self.root,"Add Operator", [
            ("system_group_id", "System group ID"),
            ("username", "Username"),
            ("role", "Role"),
            ("hire_date", "Hire date (YYYY-MM-DD)")
        ])
        if(operator is None):
            return
        #use sql