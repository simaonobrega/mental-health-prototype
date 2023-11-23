import tkinter as tk


# Standard button with pre-defined padding
class StandardButtonInGrid:
    def __init__(self, parent, button_name, row, column, command=None):
        self._button = tk.Button(parent, text=button_name, relief="raised",
                                 borderwidth=2, padx=10, pady=5, command=command)
        self._button.grid(row=row, column=column, padx=5, pady=5)
