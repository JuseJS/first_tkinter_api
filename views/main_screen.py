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

        # Frame principal de la ventana
        main_frame = ttk.Frame(self, style='TFrame')
        main_frame.pack(expand=True, fill= "both")

        # Titulo de la ventana
        title = ttk.Label(main_frame,text="Listado de Productos", style="Title.TLabel", anchor="e", justify="center")
        title.place(x= 0, y=20, width=500)
        title.update_idletasks()
        print(title.winfo_height())
        # Barra de busqueda
        ttk.Entry(main_frame, style="Search.TEntry").place(x= 625, y=20, width=300, height=30)

        self.pack(expand=True, fill= "both")

