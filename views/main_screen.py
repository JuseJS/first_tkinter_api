import tkinter as tk

from tkinter import ttk

from views.app_styles import AppStyles
from views.product_card import ProductCard


class MainScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Cargamos Los estilos
        AppStyles.configure_styles(self)

        # Frame principal de la ventana
        main_frame = ttk.Frame(self, style='TFrame')
        main_frame.pack(expand=True, fill= "both")

        # Titulo de la ventana
        title = ttk.Label(main_frame,text="Listado de Productos", style="Title.TLabel", anchor="e", justify="center")
        title.place(x= 0, y=20, width=500)
        # Barra de busqueda
        ttk.Entry(main_frame, style="Search.TEntry").place(x= 625, y=20, width=300, height=30)

        # Seccion Productos
        products_frame = ttk.Frame(main_frame, style='Section.TFrame')
        products_frame.place(x=50, y=80, width=900, height=500)

        for product in controller.products:
            product_card = ProductCard(products_frame, product)
            product_card.pack(side="top", pady=10, padx=10, anchor="w")

        self.pack(expand=True, fill= "both")

