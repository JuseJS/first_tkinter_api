from tkinter import ttk

from controllers.img_controller import ImgController


class ProductCard(ttk.Frame):
    def __init__(self, parent, product):
        super().__init__(parent)
        self.product = product
        self.configure(style="ProductCard.TFrame")

        # Obtener la imagen
        self.image = ImgController.download_image(self.product.images[0])

        # Imagen
        self.image_label = ttk.Label(self, image=self.image, style="ProductCard.TLabel")
        self.image_label.pack()

        # Titulo
        self.title_label = ttk.Label(self, text=self.product.title, style="ProductCardTitle.TLabel")
        self.title_label.pack(pady=(5, 0))

        # Descripcion
        self.description_label = ttk.Label(self, text=self.product.description, style="ProductCardDesc.TLabel", wraplength=180)
        self.description_label.pack(pady=(2, 5))

        # Hacer que el card sea clicable
        self.bind("<Button-1>", self.on_click)
        self.image_label.bind("<Button-1>", self.on_click)
        self.title_label.bind("<Button-1>", self.on_click)
        self.description_label.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        print(f"Hola {self.product.title}")

