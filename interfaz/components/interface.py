import tkinter as tk
from tkinter import messagebox
from .display import Display
from .balance import Balance
from .keypad import Keypad


class Interface(tk.Frame):
    def __init__(self, parent, checkout_func):
        super().__init__(parent)

        self.keypad_state = "INPUTTING"
        self.topline = "CONSULTAR PRECIO:"
        self.bottomline = ""

        self.checking = True

        self.display = Display(self, self.topline)
        self.balance = Balance(self, 0, lambda: self.__set_checking(False))
        self.keypad = Keypad(self, self.__keypress, checkout_func, self.__clear)

        self.display.pack(expand=True, fill=tk.BOTH, side=tk.TOP, pady=(0, 5))
        self.balance.pack(expand=True, fill=tk.BOTH, side=tk.TOP, pady=(0, 25))
        self.keypad.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)

    def __keypress(self, key):
        if self.keypad_state == "INPUTTING" and len(self.bottomline) < 2:
            self.bottomline += key
            self.display.update_display(self.topline, self.bottomline)
        if self.keypad_state == "ERROR":
            self.keypad_state = "INPUTTING"
            self.bottomline = key
            self.display.update_display(self.topline, self.bottomline)

    def __clear(self):
        self.bottomline = ""
        self.display.update_display(self.topline, self.bottomline)

    def __set_checking(self, val):
        if val:
            self.checking = val
            self.__set_topline("CONSULTAR PRECIO:")
            self.__clear()
        else:
            self.checking = val
            self.__set_topline("HACER SELECCIÓN:")

    def __set_topline(self, text):
        self.topline = text
        self.display.update_display(self.topline, self.bottomline)

    def __set_botomline(self, text):
        self.bottomline = text
        self.display.update_display(self.topline, self.bottomline)

    def get_balance(self):
        return self.balance.balance

    def get_input(self):
        return self.bottomline

    def set_error(self, error):
        self.bottomline = error
        self.keypad_state = "ERROR"
        self.display.update_display(self.topline, self.bottomline)

    def checkout(self, item):
        if self.checking:
            self.__set_botomline(f"PRECIO: ${item['price']}")
            self.keypad_state = "ERROR"
            return

        if self.balance.balance < item["price"]:
            self.__set_botomline("FONDOS INSUFICIENTES")
            self.keypad_state = "ERROR"
            return

        new_balance = self.balance.balance - item["price"]
        self.__set_botomline("")
        self.balance.update_balance(0)
        self.balance.update_change(new_balance)
        self.__set_checking(True)
        messagebox.showinfo("¡Compra Exitosa!", f"Recibiste: {item['name']}")
