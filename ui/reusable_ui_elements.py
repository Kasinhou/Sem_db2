import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime
from tkcalendar import DateEntry
from tkinter import filedialog
from pathlib import Path

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
from tkinter import ttk, filedialog, messagebox
from datetime import date, datetime
from tkcalendar import DateEntry


def open_form(root, title, fields, initial=None):
    """
    fields = [
        (column_name, label, data_type),
        ...
    ]

    Supported types: str, int, float, date, datetime, "file"

    Date formats:
        YYYY-MM-DD
        YYYY-MM-DD HH:MM
        YYYY-MM-DD HH:MM:SS

    Initial date/datetime values may be strings or Python objects.
    Blank fields return None.
    File fields return the selected path as str.
    """

    initial = initial or {}

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

        time_entry = None

        if data_type is datetime:
            frame = ttk.Frame(window)
            frame.grid(row=i, column=1, padx=10, pady=8)

            entry = DateEntry(
                frame, width=12, date_pattern="yyyy-mm-dd"
            )
            entry.grid(row=0, column=0, padx=(0, 5))

            time_entry = ttk.Entry(frame, width=10)
            time_entry.grid(row=0, column=1)
            time_entry.insert(0, "00:00:00")

        elif data_type is date:
            entry = DateEntry(
                window, width=30, date_pattern="yyyy-mm-dd"
            )
            entry.grid(row=i, column=1, padx=10, pady=8)

        elif data_type == "file":
            variable = tk.StringVar()
            entry = ttk.Entry(
                window, width=30, textvariable=variable
            )
            entry.grid(row=i, column=1, padx=10, pady=8)

            def browse(var=variable):
                path = filedialog.askopenfilename(
                    parent=window,
                    title="Select a file"
                )
                if path:
                    var.set(path)

            ttk.Button(
                window,
                text="Browse...",
                command=browse
            ).grid(row=i, column=2, padx=5, pady=8)

        else:
            entry = ttk.Entry(window, width=30)
            entry.grid(row=i, column=1, padx=10, pady=8)

        # Populate initial values
        value = initial.get(name)

        if value is not None:
            if data_type is datetime:
                if isinstance(value, str):
                    value = datetime.fromisoformat(value)
                elif not isinstance(value, datetime):
                    raise TypeError(
                        f"{name} must be a datetime or ISO string"
                    )

                entry.set_date(value.date())
                time_entry.delete(0, tk.END)
                time_entry.insert(0, value.strftime("%H:%M:%S"))

            elif data_type is date:
                if isinstance(value, datetime):
                    value = value.date()
                elif isinstance(value, str):
                    value = date.fromisoformat(value)
                elif not isinstance(value, date):
                    raise TypeError(
                        f"{name} must be a date or ISO string"
                    )

                entry.set_date(value)

            elif data_type == "file":
                entry.insert(0, str(value))

            else:
                entry.insert(0, str(value))

        entries[name] = (entry, data_type, time_entry)

    def submit():
        nonlocal result
        data = {}

        try:
            for name, (entry, data_type, time_entry) in entries.items():

                if data_type is datetime:
                    time_value = time_entry.get().strip()

                    if not time_value:
                        data[name] = None
                        continue

                    date_value = entry.get_date()

                    try:
                        parsed_time = datetime.strptime(
                            time_value, "%H:%M:%S"
                        ).time()
                    except ValueError:
                        parsed_time = datetime.strptime(
                            time_value, "%H:%M"
                        ).time()

                    converted = datetime.combine(
                        date_value, parsed_time
                    )

                else:
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
                    elif data_type == "file":
                        converted = value
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

        result = tuple(data[name] for name, *_ in fields)
        window.destroy()

    ttk.Button(
        window, text="Save", command=submit
    ).grid(row=len(fields), column=0, padx=10, pady=12)

    ttk.Button(
        window, text="Cancel", command=window.destroy
    ).grid(row=len(fields), column=1, padx=10, pady=12)

    window.wait_window()
    return result