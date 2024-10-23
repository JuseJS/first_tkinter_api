import tkinter as tk
from tkinter import ttk

from controllers.product_controller import ProductController
from views.app_styles import AppStyles


class MainScreen(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent)
        # Cargamos los estilos
        AppStyles.configure_styles(self)

        # Frame principal de la ventana
        self.main_frame = ttk.Frame(self, style='TFrame')
        self.main_frame.pack(expand=True, fill="both")

        # Titulo de la ventana
        self.title = ttk.Label(self.main_frame, text="Listado de Productos", style="Title.TLabel", anchor="e", justify="center")
        self.title.place(x=0, y=20, width=850)

        # Barra de busqueda
        self.search_entry = ttk.Entry(self.main_frame, style="Search.TEntry")
        self.search_entry.place(x=1250, y=20, width=300, height=30)

        # Seccion Productos
        self.products_canvas = tk.Canvas(self.main_frame, width=1500, height=540)
        self.products_canvas.place(x=50, y=80)

        self.h_scrollbar = ttk.Scrollbar(self.main_frame, orient="horizontal", style='TScrollbar', command=self.products_canvas.xview)
        self.h_scrollbar.place(x=50, y=620, width=1500)

        self.products_frame = ttk.Frame(self.products_canvas, style='Section.TFrame')
        self.products_frame.bind("<Configure>", lambda e: self.configure_scrollregion())
        self.products_canvas.create_window((0, 0), window=self.products_frame, anchor="nw")

        self.products_canvas.configure(xscrollcommand=self.h_scrollbar.set)

        # Muestro los cards de los productos
        ProductController.show_products_cards(self.products_frame, controller)

        self.place(x=0, y=0, relwidth=1, relheight=1)

    def configure_scrollregion(self):
        self.products_canvas.configure(scrollregion=self.products_canvas.bbox("all"))
