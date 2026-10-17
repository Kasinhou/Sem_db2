
import tkinter as tk
from tkinter import ttk

import src.db as db
from ui.people_menu import People_menu
from ui.system_group_menu import System_group_menu
from ui.report_menu import Report_menu

from ui.modules.attachment_module import Attachment_module
from ui.modules.call_report_module import Call_report_module
from ui.modules.case_file_module import Case_file_module
from ui.modules.case_note_module import Case_note_module
from ui.modules.case_unit_module import Case_unit_assignment_module
from ui.modules.contact_module import Contact_module
from ui.modules.fault_report_module import Fault_report_module
from ui.modules.operator_module import Operator_modul
from ui.modules.person_module import Person_modul
from ui.modules.system_group_module import System_group_module
from ui.modules.unit_module import Unit_module
from ui.modules.unit_type_module import Unit_type_module

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Emergency respond system")
        self.root.geometry("1920x1080")

        #module iit
        self.person_module = Person_modul(self.root)
        self.contact_module = Contact_module(self.root, self.person_module)
        self.operator_module = Operator_modul(self.root, self.person_module)
        self.fault_report_module = Fault_report_module(self.root, self.operator_module)
        self.call_report_module = Call_report_module(self.root, self.operator_module)
        self.case_file_module = Case_file_module(self.root, self.operator_module)
        self.case_unit_ass_module = Case_unit_assignment_module(self.root, self.case_file_module)
        self.attachment_module = Attachment_module(self.root, self.case_file_module)
        self.case_note_module = Case_note_module(self.root, self.case_file_module)
        self.group_module = System_group_module(self.root)
        self.unit_module = Unit_module(self.root, self.group_module)
        self.unit_type_module = Unit_type_module(self.root, self.group_module)


        # Menu bar
        self.menubar = tk.Menu(root)

        self.menu = tk.Menu(self.menubar, tearoff=0)
        self.menu.add_command(
            label="People",
            command=self.show_people
        )
        self.menu.add_command(
            label="System Group",
            command=self.show_system_group_menu
        )
        self.menu.add_command(
            label="Report",
            command=self.show_report_menu
        )
        self.menu.add_separator()
        self.menu.add_command(
            label="Exit",
            command=self.root.destroy
        )

        self.menubar.add_cascade(
            label="Menu",
            menu=self.menu
        )
        self.root.config(menu=self.menubar)

        # Content area for the selected menu
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.pack(fill="both", expand=True)

        self.current_menu = None

    def clear_menu(self):
        """Remove the current menu and its widgets."""
        if self.current_menu is not None:
            self.current_menu.destroy()
            self.current_menu = None

        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_people(self):
        self.clear_menu()

        self.current_menu = ttk.Frame(self.content_frame)
        self.current_menu.pack(fill="both", expand=True)

        People_menu(self.current_menu, self.person_module, self.operator_module, self.contact_module)

    def show_system_group_menu(self):
        self.clear_menu()

        self.current_menu = ttk.Frame(self.content_frame)
        self.current_menu.pack(fill="both", expand=True)

        System_group_menu(self.current_menu, self.group_module, self.unit_module, self.unit_type_module)

    def show_report_menu(self):
        self.clear_menu()

        self.current_menu = ttk.Frame(self.content_frame)
        self.current_menu.pack(fill="both", expand=True)

        Report_menu(self.current_menu, self.operator_module, self.call_report_module, self.case_file_module, self.fault_report_module, self.case_unit_ass_module, self.attachment_module, self.case_note_module)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()