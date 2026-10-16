import tkinter as tk
from tkinter import ttk, messagebox
from ui.reusable_ui_elements import setup_table, open_form, update_table_columns
from datetime import date, datetime

class System_group_menu:
    def __init__(self, root):
        self.root = root
        self.current_view = 0 #0 - system_groups, 1 - units, 2 - unit_types;
        self.selected_system_group = None
        self.selected_unit = None
        self.selected_unit_type = None
        self.bigest_system_group_id = 0
        self.bigest_unit_id = 0
        self.bigest_unit_type_id = 0

        #temp before sql
        self.system_groups = [(0, None, "Blavacky Hasici", "Bratislava")]
        self.units = [(0,0,0,"CAS 30","available","gps_object","equipment_collection","path_to_photo")]
        self.unit_types = [(0, "A56", "hasici")]
        
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
            command=self.add_system_group
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            top_buttons,
            text="Add Unit Type",
            command=self.add_unit_type
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
            ("Add Unit", self.add_unit),
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
    
    def add_system_group(self):
        group = open_form(self.root,"Add System group", [
            ("parent_group_id", "Parent group id", int),
            ("name", "Name", str),
            ("region", "Region", str)
        ])

        if(group is None):
            return
        
        #use sql to save person

        self.bigest_system_group_id += 1
        group = (self.bigest_system_group_id , *group)

        self.system_groups.append(group)
        self.load_data()

    def edit_system_group(self):
        if self.selected_system_group is None:
            return

        values = self.tree.item(self.selected_system_group, "values")

        group = open_form(self.root,"Edit System group", [
            ("parent_group_id", "Parent group id", int),
            ("name", "Name", str),
            ("region", "Region", str)
        ], {
            "parent_group_id": values[0],
            "name": values[1],
            "region": values[2]
        })
        if(group is None):
            return

        self.tree.item(self.selected_system_group, values=group)  
        for i in range(len(self.system_groups)):
            if self.system_groups[i][0] == self.selected_system_group:
                self.system_groups[i] = group 
                break
        #use sql to save person        

    def edit_unit(self):
        if self.selected_unit_type is None:
            return

        values = self.tree.item(self.selected_unit, "values")

        unit = open_form(self.root,"Edit Contact Info", [
            ("unit_type_id", "Unit Type ID", int),
            ("call_sign", "Call Sign", str),
            ("status", "Status", str),
            ("last_position", "Last Postion", str),
            ("equipment", "Equipment", str),
            ("photo", "Phooto", str)
        ], {
            "unit_type_id": values[0],
            "call_sign": values[1],
            "status": values[2],
            "last_position": values[3],
            "equipment": values[4],
            "photo": values[5],
        })
        if(unit is None):
            return

        self.tree.item(self.selected_unit, values=unit)  
        for i in range(len(self.units)):
            if self.units[i][0] == self.selected_unit:
                self.units[i] = unit 
                break
        #use sql to save contact        

    def edit_unit_type(self):
        if self.selected_unit_type is None:
            return

        values = self.tree.item(self.selected_unit_type, "values")
        unit_type = open_form(self.root,"Edit Operator Info", [
            ("code", "Code", str),
            ("name", "Name", str)
        ], {
            "code": values[0],
            "name": values[1]
        })
        if(unit_type is None):
            return

        self.tree.item(self.selected_unit_type, values=unit_type)  
        for i in range(len(self.unit_types)):
            if self.unit_types[i][0] == self.selected_unit_type:
                self.unit_types[i] = unit_type 
                break
        #use sql to save operator        
    
    def delete_system_group(self):
        if self.selected_system_group is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this group?"
        ):
            return

        #ADD SQL
        for i in range(len(self.system_groups)):
            if self.system_groups[i][0] == self.selected_system_group:
                self.system_groups.remove(self.system_groups[i])
                break
        
        self.selected_system_group = None

    def delete_unit(self):
        if self.selected_unit_type is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this unit?"
        ):
            return

        #ADD SQL
        for i in range(len(self.units)):
            if self.units[i][0] == self.selected_unit:
                self.units.remove(self.units[i])
                break
        
        self.selected_unit = None
    
    def delete_unit_type(self):
        if self.selected_unit_type is None:
            return

        if not messagebox.askyesno(
            "Confirm delete",
            "Do you really want to delete this unit type?"
        ):
            return

        #ADD SQL
        for i in range(len(self.unit_types)):
            if self.unit_types[i][0] == self.selected_unit_type:
                self.unit_types.remove(self.unit_types[i])
                break
        
        self.selected_unit_type = None    

    def load_data(self):
        #Write select here
        
        self.tree.delete(*self.tree.get_children())

        match self.current_view:
            case 0:
                for row in self.system_groups:
                    self.tree.insert("", "end", iid=row[0], values=row)
            case 1:
                for row in self.units:
                    self.tree.insert("", "end", iid=row[0], values=row)
            case 2:
                for row in self.unit_types:
                    self.tree.insert("", "end", iid=row[0], values=row)

        self.selected_system_group = None
        self.selected_unit = None
        self.selected_unit_type = None
        for button in self.action_buttons:
            button.config(state="disabled")


    def on_selected(self, event=None):
        selected = self.tree.selection()

        if selected:
            match self.current_view:
                case 0:
                    self.selected_system_group = int(selected[0])
                    for button in self.action_buttons:
                        button.config(state="normal")
                case 1:
                    self.selected_unit = int(selected[0])                
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
                case 2:
                    self.selected_unit_type = int(selected[0])               
                    for i in range(2):
                        self.action_buttons[i].config(state="normal")
        else:
            self.selected_system_group = None
            self.selected_unit = None
            self.selected_unit_type = None

            for button in self.action_buttons:
                button.config(state="disabled")

    def add_unit(self):
        if self.selected_system_group is None:
            return

        unit = open_form(self.root,"Add Unit", [
            ("unit_type_id", "Unit Type ID", int),
            ("call_sign", "Call Sign", str),
            ("status", "Status", str),
            ("last_position", "Last Postion", str),
            ("equipment", "Equipment", str),
            ("photo", "Phooto", str)
        ])
        if(unit is None):
            return
        #use sql
        self.bigest_unit_id += 1
        self.units.append((self.bigest_unit_id, unit[0], self.selected_system_group, *unit[1:]))
        self.current_view = 1
        self.update_view_table()

    def add_unit_type(self):

        unit_type = open_form(self.root,"Add Unit Type", [
            ("code", "Code", str),
            ("name", "Name", str)
        ])
        if(unit_type is None):
            return
        #use sql
        self.bigest_unit_type_id += 1
        self.unit_types.append((self.bigest_unit_type_id ,*unit_type))
        self.current_view = 2
        self.update_view_table()
    
    def update_view_table(self):
        match self.current_view:
            case 0:
                des = ["system_group_id", "parent_group_id", "name", "region"]       
                update_table_columns(self.tree, des)
            case 1:
                des = ["unit_id", "unit_type_id", "system_group_id", "call_sign", "status", "last_position", "equipment", "photo"]       
                update_table_columns(self.tree, des)
            case 2:
                des = ["unit_type_id", "code", "name"]        
                update_table_columns(self.tree, des)
        self.load_data()


    def edit_data(self):
        match self.current_view:
            case 0:
                self.edit_system_group()
            case 1:
                self.edit_unit()
            case 2:
                self.edit_unit_type()

    def delete_data(self):
        match self.current_view:
            case 0:
                self.delete_system_group()
            case 1:
                self.delete_unit()
            case 2:
                self.delete_unit_type()
        self.load_data()
        

