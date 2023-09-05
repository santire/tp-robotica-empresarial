import tkinter as tk


class Keypad(tk.Frame):
    def __init__(self, parent, keypress, ok, clear):
        super().__init__(parent)

        button_font = ("Arial", 20)
        button_bg = "lightgray"
        button_fg = "black"

        self.pack(pady=10)

        keypad_buttons = [
            "1",
            "2",
            "A",
            "3",
            "4",
            "B",
            "5",
            "6",
            "C",
            "7",
            "8",
            "D",
            "9",
            "0",
            "E",
            "OK",
            "Clear",
        ]

        row_num, col_num = 0, 0

        for key in keypad_buttons[:-2]:
            button = tk.Button(
                self,
                text=key,
                font=button_font,
                width=4,
                height=2,
                bg=button_bg,
                fg=button_fg,
                command=lambda key=key: keypress(key),
            )
            button.grid(row=row_num, column=col_num, padx=5, pady=5)
            col_num += 1
            if col_num > 2:
                col_num = 0
                row_num += 1
        ok_button = tk.Button(
            self,
            text="OK",
            font=button_font,
            width=4,
            height=2,
            bg=button_bg,
            fg=button_fg,
            command=lambda _="OK": ok(),
        )
        ok_button.grid(row=row_num, column=col_num, padx=5, pady=5)
        cancel_button = tk.Button(
            self,
            text="CLR",
            font=button_font,
            width=4,
            height=2,
            bg=button_bg,
            fg=button_fg,
            command=lambda _="CLR": clear(),
        )
        cancel_button.grid(row=row_num, column=col_num + 1, padx=5, pady=5)
