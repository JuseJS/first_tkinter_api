import tkinter as tk

from tkinter import ttk

from views.app_styles import AppStyles

class ProductCard(ttk.Frame):
    def __init__(self, parent, product):
        super().__init__(parent)

        # Cargamos Los estilos
        AppStyles(self)
        self.style = ttk.Style()

        # Frame principal de la ventana
        main_frame = ttk.Frame(self, style='TFrame')
        main_frame.pack(expand=True, fill= "both")

        # Titulo de la ventana
        title = ttk.Label(main_frame,text=product.title, style="Title.TLabel", anchor="e", justify="center")
        title.pack()

        self.pack(expand=True, fill= "both")

