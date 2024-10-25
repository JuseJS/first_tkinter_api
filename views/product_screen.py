import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

from controllers.img_controller import ImgController
from views.app_styles import AppStyles


class ProductScreen(ttk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent)
        self.product = args[0]
        self.controller = controller

        # Cargamos los estilos
        AppStyles.configure_styles(self)

        # Frame principal de la ventana
        self.main_frame = ttk.Frame(self, style='TFrame')
        self.main_frame.pack(expand=True, fill="both")

        # Titulo del Producto
        self.title = ttk.Label(self.main_frame, text=self.product.title, style="Title.TLabel", anchor="center", justify="center")
        self.title.place(x=0, y=20, width=1600)

        # Boton para volver a inicio
        self.back_btn = ttk.Button(self.main_frame, text="← Volver", style="TButton", command=self.volver_atras)
        self.back_btn.place(x=20, y=20, width=140, height=45)

        # Canvas para hacer un scroll con la info
        self.product_info_canvas = tk.Canvas(self.main_frame, width=1500, height=650)
        self.product_info_canvas.place(x=50, y=100)

        # Scrollbar
        self.v_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", style='TScrollbar',
                                         command=self.product_info_canvas.yview)
        self.v_scrollbar.place(x=1550, y=100, height=650)

        self.product_info_canvas.configure(yscrollcommand=self.v_scrollbar.set)

        # Frame de la informacion del producto
        self.product_info_frame = ttk.Frame(self.product_info_canvas, style='Section.TFrame')
        self.product_info_canvas.create_window((0, 0), window=self.product_info_frame, anchor="nw")

        self.product_info_frame.bind("<Configure>", lambda e: self.configure_scrollregion())

        # Imagen de carga
        self.loading_image = ImageTk.PhotoImage(Image.new('RGB', (500, 500), (44, 44, 46)))
        self.image_label = ttk.Label(self.product_info_frame, image=self.loading_image, style="ProductCard.TLabel")
        self.image_label.pack(padx=(20, 20), pady=(20, 10))

        # Carga imagen y la actualiza
        ImgController.update_image_label(self.image_label, self.product.images[0], (500, 500))

        # Descripción
        self.description_label = ttk.Label(self.product_info_frame, text=self.product.description, style="ProductCardDesc.TLabel",
                                           wraplength=280, anchor='w', justify='left')
        self.description_label.pack(pady=(5, 5), side="left")

        # Precio
        price_text = "Precio: " + str(self.product.price) + "€"
        print(price_text)
        self.price_label = ttk.Label(self.product_info_frame, text=price_text, style="ProductCardDesc.TLabel",
                                           wraplength=280, anchor='w', justify='left')
        self.price_label.pack(pady=(5, 5), side="left")

        self.place(x=0, y=0, relwidth=1, relheight=1)

    def volver_atras(self):
        from views.main_screen import MainScreen
        self.controller.show_frame(MainScreen)

    def configure_scrollregion(self):
        self.product_info_canvas.configure(scrollregion=self.product_info_canvas.bbox("all"))
