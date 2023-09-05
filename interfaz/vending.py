import tkinter as tk
from components.interface import Interface


class VendingMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina Expendedora")
        self.items = {
            "A1": {"name": "Coca Cola", "price": 15},
            "A2": {"name": "Pringles", "price": 10},
            "A3": {"name": "Alfajor", "price": 7.5},
            "A4": {"name": "Agua", "price": 12.5},
            "B1": {"name": "Oreos", "price": 17.5},
            "B2": {"name": "Beldent", "price": 5},
            "B3": {"name": "Cepita", "price": 18},
            "B4": {"name": "Cerealmix", "price": 19},
            "C1": {"name": "Pepsi", "price": 15},
            "C2": {"name": "Express", "price": 8},
            "C3": {"name": "Tita", "price": 5.5},
            "C4": {"name": "Aquarius", "price": 13.5},
            "D1": {"name": "Oreos", "price": 7.5},
            "D2": {"name": "Halls", "price": 3},
            "D3": {"name": "Mani", "price": 4},
            "D4": {"name": "Mix nueces", "price": 14},
        }

        row_num, col_num = 0, 0
        items_grid = tk.Frame(root)
        for item_key in self.items.keys():
            itm = self.items[item_key]
            frame = tk.Frame(items_grid)
            itembox = tk.Label(frame, text=f"{itm['name']}", font=("Arial", 16))
            itembox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            itemkey = tk.Label(frame, text=f"{item_key}", font=("Arial", 11))
            itembox.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)
            itemkey.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)

            frame.grid(row=row_num, column=col_num, padx=5, pady=25)
            col_num += 1
            if col_num > 3:
                col_num = 0
                row_num += 1

        self.interface = Interface(root, self.__purchase)
        self.interface.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT, padx=20, pady=40)
        items_grid.config(highlightbackground="black", highlightthickness=3)
        items_grid.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=20, pady=40)

    def __purchase(self):
        input = self.interface.get_input()
        item = self.items.get(input, None)
        if item is None:
            self.interface.set_error("ITEM INVÁLIDO")
        else:
            self.interface.checkout(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineApp(root)
    root.mainloop()
