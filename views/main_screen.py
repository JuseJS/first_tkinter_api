import tkinter as tk

from tkinter import ttk

from views.app_styles import AppStyles
from views.product_card import ProductCard

class MainScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Cargamos Los estilos
        AppStyles(self)
        self.style = ttk.Style()

        ttk.Frame(self, style='TFrame').pack(expand=True, fill= "both")
        self.pack(expand=True, fill= "both")

