import tkinter as tk
from tkinter import ttk

from views.main_screen import MainScreen


class MainApp(tk.Tk):
    def __init__(self, title, size, controller):
        super().__init__()
        self.title(title)
        self.geometry(size)

        self.main_screen = MainScreen(self, controller)
        self.mainloop()

