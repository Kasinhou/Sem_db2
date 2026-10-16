import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime
from tkcalendar import DateEntry

def get_table_as_string(description, data) -> str :
    result = ''

    for i in range(len(data)):
        for j in range(len(description)):
            result += description[j] + "\t" + data[i][j]
            
    return result

def show_table(root, description, data) :
    
    tree = setup_table(root, description)
    # Insert database rows
    for row in data:
        tree.insert("", "end", values=row)

    return tree

def update_table_columns(tree, description):
    tree["columns"] = description
    tree["show"] = "headings"

    for col in description:
        tree.heading(col, text=col)
        tree.column(col, width=130, minwidth=80, anchor="w")

def setup_table(root, description):
    table_frame = ttk.Frame(root)
    table_frame.pack(fill="both", expand=True, padx=10, pady=5)

    tree = ttk.Treeview(table_frame, show="headings")

    vertical_scroll = ttk.Scrollbar(
        table_frame, orient="vertical", command=tree.yview
    )
    horizontal_scroll = ttk.Scrollbar(
        table_frame, orient="horizontal", command=tree.xview
    )

    tree.configure(
        yscrollcommand=vertical_scroll.set,
        xscrollcommand=horizontal_scroll.set
    )

    tree.grid(row=0, column=0, sticky="nsew")
    vertical_scroll.grid(row=0, column=1, sticky="ns")
    horizontal_scroll.grid(row=1, column=0, sticky="ew")

    table_frame.rowconfigure(0, weight=1)
    table_frame.columnconfigure(0, weight=1)

    ttk.Label(root, text="Ready").pack(anchor="w", padx=10, pady=5)

    update_table_columns(tree, description)

    return tree

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date


def open_form(root, title, fields, initial=None):
    """
    fields = [
        (column_name, label, data_type),
        ...
    ]

    Supported types: str, int, float, date
    Date format: YYYY-MM-DD
    """
    window = tk.Toplevel(root)
    window.title(title)
    window.transient(root)
    window.grab_set()

    entries = {}
    result = None

    for i, (name, label, data_type) in enumerate(fields):
        ttk.Label(window, text=label).grid(
            row=i, column=0, padx=10, pady=8, sticky="w"
        )

        entry = ttk.Entry(window, width=30) if data_type != date else DateEntry(window, width=30, date_pattern="yyyy-mm-dd")
        entry.grid(row=i, column=1, padx=10, pady=8)

        if initial and name in initial:
            value = initial[name]

            if data_type is date and isinstance(value, date):
                value = value.isoformat()

            entry.insert(0, str(value))

        entries[name] = (entry, data_type)

    def submit():
        nonlocal result
        data = {}

        try:
            for name, (entry, data_type) in entries.items():
                value = entry.get().strip()

                if not value:                    
                    data[name] = None
                    continue

                if data_type is str:
                    converted = value
                elif data_type is int:
                    converted = int(value)
                elif data_type is float:
                    converted = float(value)
                elif data_type is date:
                    converted = entry.get_date()
                else:
                    raise ValueError(
                        f"Unsupported data type: {data_type}"
                    )

                data[name] = converted

        except ValueError as e:
            messagebox.showwarning(
                "Invalid data",
                f"Please check your input.\n\n{e}",
                parent=window
            )
            return

        result = tuple(data.values())
        window.destroy()

    ttk.Button(
        window, text="Save", command=submit
    ).grid(row=len(fields), column=0, padx=10, pady=12)

    ttk.Button(
        window, text="Cancel", command=window.destroy
    ).grid(row=len(fields), column=1, padx=10, pady=12)

    window.wait_window()
    return result