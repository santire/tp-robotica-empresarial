import tkinter as tk
from tkinter import simpledialog


class Balance(tk.Frame):
    def __init__(self, parent, balance, on_success):
        super().__init__(parent)
        self.balance = balance

        self.frame = tk.Frame(self)
        self.display_label = tk.Label(
            self.frame, text=f"Balance actual: ${balance}", font=("Arial", 12)
        )
        self.change_label = tk.Label(self, text="", font=("Arial", 12))

        self.display_label.pack(pady=20, fill=tk.BOTH, side=tk.LEFT, padx=10)
        self.change_label.pack(pady=2, fill=tk.BOTH, side=tk.BOTTOM, padx=10)
        self.frame.pack(fill=tk.BOTH, side=tk.BOTTOM)

        def open_number_input_window():
            number = simpledialog.askinteger(
                "Cargar dinero", "Ingrese un número:", minvalue=1, maxvalue=200
            )
            if number is not None:
                self.balance += number
                self.display_label.config(text=f"Balance actual: ${self.balance}")
                on_success()

        open_button = tk.Button(
            self.frame, text="Cargar dinero", command=open_number_input_window
        )
        open_button.pack(
            expand=True, fill=tk.BOTH, side=tk.RIGHT, padx=(15, 10), pady=10
        )

        self.frame.config(highlightbackground="black", highlightthickness=1)

    def update_balance(self, new_balance):
        self.balance = new_balance
        self.display_label.config(text=f"Balance actual: ${self.balance}")

    def update_change(self, change):
        self.change_label.config(text=f"Cambio: ${change}")
