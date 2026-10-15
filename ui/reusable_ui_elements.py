import tkinter as tk
from tkinter import ttk, messagebox

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

def setup_table(root, description):

    # Table container
    table_frame = ttk.Frame(root)
    table_frame.pack(fill="both", expand=True, padx=10, pady=5)

    # Table with scrollbars
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

    status_label = ttk.Label(root, text="Ready")
    status_label.pack(anchor="w", padx=10, pady=5)

    # Define the table columns dynamically
    tree["columns"] = description

    # Remove previous data and headings
    tree.delete(*tree.get_children())

    tree["show"] = "headings"

    for col in description:
        tree.heading(col, text=col)
        tree.column(col, width=130, minwidth=80, anchor="w")

    return tree

def open_form(root, title, fields, initial=None):
    """Reusable form. fields = [(column_name, label), ...]"""
    window = tk.Toplevel(root)
    window.title(title)
    window.transient(root)
    window.grab_set()

    entries = {}
    result = None

    for i, (name, label) in enumerate(fields):
        ttk.Label(window, text=label).grid(
            row=i, column=0, padx=10, pady=8, sticky="w"
        )

        entry = ttk.Entry(window, width=30)
        entry.grid(row=i, column=1, padx=10, pady=8)

        if initial and name in initial:
            entry.insert(0, str(initial[name]))

        entries[name] = entry

    def submit():
        nonlocal result
        data = {name: entry.get().strip()
                for name, entry in entries.items()}

        if any(not value for value in data.values()):
            messagebox.showwarning(
                "Missing data",
                "Please fill in all fields.",
                parent=window
            )
            return

        result = tuple(data.values())
        window.destroy()

    ttk.Button(
        window, text="Save", command= submit
    ).grid(
        row=len(fields), column=0, padx=10, pady=12
    )

    ttk.Button(
        window, text="Cancel", command=window.destroy
    ).grid(
        row=len(fields), column=1, padx=10, pady=12
    )
    window.wait_window()

    return result