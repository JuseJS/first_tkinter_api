import tkinter as tk
from tkinter import ttk

from views.app_styles import AppStyles
from views.main_screen import MainScreen


class MainApp(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(size)

        self.main_screen = MainScreen(self)
        self.mainloop()

def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()