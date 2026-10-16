import tkinter as tk
from tkinter import ttk, messagebox
from ui.reusable_ui_elements import setup_table, open_form, update_table_columns
from datetime import date, datetime

class People_menu:
    def __init__(self, root):
        self.root = root
        self.current_view = 0 #0 - people, 1 - contacts, 2 - operators;
        self.selected_person = None
        self.selected_contact = None
        self.selected_operator = None
        self.bigest_contact_id = 0
        self.bigest_operator_id = 0

        #temp before sql
        self.people = [("841106/3456","Jozko","Mrkvicka"),("855130/3695","Magdalena","Mrkvova"),("850130/3695","Mojmir","Kovac"),("845312/7845","Marisa","Clnkova")]
        self.contacts = [(0,"090315676","841106/3456")]
        self.operators = [(0,0,"Magda","someone",datetime.now(),"855130/3695")]
        
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
            command=self.add_person
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
            ("personal_id_number", "Personal identification number", str),
            ("first_name", "First name", str),
            ("last_name", "Last name", str)
        ])

        if(person is None):
            return
        
        #use sql to save person

        self.people.append(person)
        self.load_data()

    def edit_person(self):
        if not self.selected_person:
            return

        values = self.tree.item(self.selected_person, "values")

        person = open_form(self.root,"Edit Personal Info", [
            ("original_personal_id_number", "Personal identification number (read-only ID)", str),
            ("first_name", "First name", str),
            ("last_name", "Last name", str)
        ], {
            "original_personal_id_number": values[0],
            "first_name": values[1],
            "last_name": values[2]
        })
        if(person is None):
            return

        self.tree.item(self.selected_person, values=person)  
        for i in range(len(self.people)):
            if self.people[i][0] == self.selected_person:
                self.people[i] = person 
                break
        #use sql to save person        

    def edit_contact(self):
        if self.selected_contact is None:
            return

        values = self.tree.item(self.selected_contact, "values")

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

        self.tree.item(self.selected_contact, values=contact)  
        for i in range(len(self.contacts)):
            if self.contacts[i][0] == self.selected_contact:
                self.contacts[i] = contact 
                break
        #use sql to save contact        

    def edit_operator(self):
        if self.selected_operator is None:
            return

        values = self.tree.item(self.selected_operator, "values")
        "operator_id","system_group_id","username","role","hire_date","personal_id_number"
        operator = open_form(self.root,"Edit Operator Info", [
            ("operator_id", "Operator ID (read-only ID)", int),
            ("system_group_id", "System group id name", int),
            ("username", "Username", str),
            ("role", "Role", str),
            ("hire date", "Hire date", date),
            ("personal id number", "Personal identification number", str)
        ], {
            "operator_id": values[0],
            "system_group_id": values[1],
            "username": values[2],
            "role": values[3],
            "hire date": values[4],
            "personal id number": values[5]
        })
        if(operator is None):
            return

        self.tree.item(self.selected_operator, values=operator)  
        for i in range(len(self.operators)):
            if self.operators[i][0] == self.selected_operator:
                self.operators[i] = operator 
                break
        #use sql to save operator        
    
    def delete_person(self):
        if not self.selected_person:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this person?"
        ):
            return

        #ADD SQL
        for i in range(len(self.people)):
            if self.people[i][0] == self.selected_person:
                self.people.remove(self.people[i])
                break
        
        self.selected_person = None

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
    
    def delete_operator(self):
        if self.selected_operator is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this operator?"
        ):
            return

        #ADD SQL
        for i in range(len(self.operators)):
            if self.operators[i][0] == self.selected_operator:
                self.operators.remove(self.operators[i])
                break
        
        self.selected_operator = None    

    def load_data(self):
        #Write select here
        
        self.tree.delete(*self.tree.get_children())

        match self.current_view:
            case 0:
                for row in self.people:
                    self.tree.insert("", "end", iid=row[0], values=row)
            case 1:
                for row in self.contacts:
                    self.tree.insert("", "end", iid=row[0], values=row)
            case 2:
                for row in self.operators:
                    self.tree.insert("", "end", iid=row[0], values=row)

        self.selected_person = None
        self.selected_contact = None
        self.selected_operator = None
        for button in self.action_buttons:
            button.config(state="disabled")


    def on_selected(self, event=None):
        selected = self.tree.selection()

        if selected:
            match self.current_view:
                case 0:
                    self.selected_person = selected[0]
                    for button in self.action_buttons:
                        button.config(state="normal")
                case 1:
                    self.selected_contact = int(selected[0])                
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
                case 2:
                    self.selected_operator = int(selected[0])               
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
        else:
            self.selected_person = None
            self.selected_contact = None
            self.selected_operator = None

            for button in self.action_buttons:
                button.config(state="disabled")

    def add_contact(self):
        if not self.selected_person:
            return

        contact = open_form(self.root,"Add Contact", [
            ("phone_number", "Phone number", str)
        ])
        if(contact is None):
            return
        #use sql
        self.bigest_contact_id+=1
        self.contacts.append((self.bigest_contact_id,contact[0],self.selected_person))
        self.current_view = 1
        self.update_view_table()

    def add_operator(self):
        if not self.selected_person:
            return

        operator = open_form(self.root,"Add Operator", [
            ("system_group_id", "System group ID", int),
            ("username", "Username", str),
            ("role", "Role", str),
            ("hire_date", "Hire date (YYYY-MM-DD)", date)
        ])
        if(operator is None):
            return
        #use sql
        self.bigest_operator_id += 1
        self.operators.append((self.bigest_operator_id,operator[0],operator[1],operator[2],operator[3],self.selected_person))
        self.current_view = 2
        self.update_view_table()
    
    def update_view_table(self):
        match self.current_view:
            case 0:
                des = ["personal_id_number", "first_name", "last_name"]        
                update_table_columns(self.tree, des)
            case 1:
                des = ["contact_id", "phone_number", "personal_id_number"]        
                update_table_columns(self.tree, des)
            case 2:
                des = ["operator_id","system_group_id","username","role","hire_date","personal_id_number"]        
                update_table_columns(self.tree, des)
        self.load_data()


    def edit_data(self):
        match self.current_view:
            case 0:
                self.edit_person()
            case 1:
                self.edit_contact()
            case 2:
                self.edit_operator()

    def delete_data(self):
        match self.current_view:
            case 0:
                self.delete_person()
            case 1:
                self.delete_contact()
            case 2:
                self.delete_operator()
        self.load_data()
        

