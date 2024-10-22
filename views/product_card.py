from tkinter import ttk
from PIL import Image, ImageTk
from controllers.img_controller import ImgController

class ProductCard(ttk.Frame):
    def __init__(self, parent, product):
        super().__init__(parent)
        self.product = product
        self.configure(style="ProductCard.TFrame",
                       width=360,
                       height=520)
        self.pack_propagate(False)

        # Imagen de carga
        self.loading_image = ImageTk.PhotoImage(Image.new('RGB', (300, 300), (200, 200, 200)))
        self.image_label = ttk.Label(self, image=self.loading_image, style="ProductCard.TLabel")
        self.image_label.pack(padx=(20, 20), pady=(20, 10))

        # Título
        self.title_label = ttk.Label(self, text=self.product.title, style="ProductCardTitle.TLabel",  wraplength=300, anchor='center', justify='center')
        self.title_label.pack(pady=(5, 0))

        # Descripción
        self.description_label = ttk.Label(self, text=self.product.description, style="ProductCardDesc.TLabel", wraplength=280, anchor='w', justify='left')
        self.description_label.pack(pady=(5, 5))

        # Hacer que el card sea clicable
        self.bind("<Button-1>", self.on_click)
        self.image_label.bind("<Button-1>", self.on_click)
        self.title_label.bind("<Button-1>", self.on_click)
        self.description_label.bind("<Button-1>", self.on_click)

        # Carga imagen y la actualiza
        ImgController.update_image_label(self.image_label, self.product.images[0])

    def on_click(self, event):
        print(f"Hola {self.product.title}")
