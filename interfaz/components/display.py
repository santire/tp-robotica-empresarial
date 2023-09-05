import tkinter as tk


class Display(tk.Frame):
    def __init__(self, parent, topline="", bottomline=""):
        super().__init__(parent)

        self.topline = topline
        self.bottomline = bottomline

        self.configure(bg="lime green")
        self.display_label = tk.Label(
            self,
            text=f"{self.topline}\n{self.bottomline}",
            font=("Courier", 18),
            fg="black",
            bg="lime green",
            width=20,
            height=4,
        )
        self.display_label.pack(padx=20, pady=20)

    def update_display(self, topline, bottomline):
        self.topline = topline
        self.bottomline = bottomline
        self.display_label.config(text=f"{self.topline}\n{self.bottomline}")
