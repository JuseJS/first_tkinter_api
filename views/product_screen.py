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
        self.title.pack(pady=20)

        # Boton para volver a inicio
        self.back_btn = ttk.Button(self.main_frame, text="← Volver", style="TButton", command=self.volver_atras)
        self.back_btn.place(x=20, y=20, width=140, height=45)

        # Canvas para hacer un scroll con la info
        self.product_info_canvas = tk.Canvas(self.main_frame)
        self.product_info_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=(0, 20))

        # Scrollbar
        self.v_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", style='TScrollbar',
                                         command=self.product_info_canvas.yview)
        self.v_scrollbar.pack(side="right", fill="y", pady=(0, 20))

        self.product_info_canvas.configure(yscrollcommand=self.v_scrollbar.set)

        # Frame de la informacion del producto
        self.product_info_frame = ttk.Frame(self.product_info_canvas, style='ProductInfo.TFrame')
        self.canvas_window = self.product_info_canvas.create_window((0, 0), window=self.product_info_frame, anchor="nw")

        self.product_info_frame.bind("<Configure>", lambda e: self.configure_scrollregion())
        self.product_info_canvas.bind("<Configure>", self.on_canvas_configure)

        # Tamaño de las columnas
        self.product_info_frame.columnconfigure(0, weight=4)
        self.product_info_frame.columnconfigure(1, weight=1)
        self.product_info_frame.columnconfigure(2, weight=5)

        # Imagen del Producto
        self.loading_image = ImageTk.PhotoImage(Image.new('RGB', (500, 500), (44, 44, 46)))
        self.image_label = ttk.Label(self.product_info_frame, image=self.loading_image, style="ProductInfoImage.TLabel")
        self.image_label.grid(row=0, column=0, padx=(0, 0), pady=(80, 10), sticky='n')

        # Carga imagen y la actualiza
        ImgController.update_image_label(self.image_label, self.product.images[0], (500, 500))

        # Información del Producto
        info_frame = ttk.Frame(self.product_info_frame, style='ProductInfo.TFrame')
        info_frame.grid(row=0, column=2, padx=(20, 20), pady=(20, 10), sticky='nsew')

        self.category_label = ttk.Label(info_frame, text=f"Categoría: {self.product.category}",
                                        style="ProductCategory.TLabel",
                                        anchor='e',
                                        justify='right')
        self.category_label.pack(anchor='e', pady=(0, 30))

        self.description_title = ttk.Label(info_frame, text="Descripción",
                                           style="ProductInfoTitle.TLabel",
                                           anchor='w',
                                           justify='left')
        self.description_title.pack(anchor='w', pady=(0, 10))
        self.description_label = ttk.Label(info_frame, text=self.product.description,
                                           style="ProductInfoText.TLabel",
                                           wraplength=500,
                                           anchor='w',
                                           justify='left')
        self.description_label.pack(anchor='w', pady=(0, 50))

        # Precio
        original_price = self.product.price
        discount_percentage = self.product.discount_percentage
        discounted_price = original_price * (1 - discount_percentage / 100)

        price_frame = ttk.Frame(info_frame, style='ProductInfo.TFrame')
        price_frame.pack(anchor='w', pady=(0, 10))

        self.final_price_text = ttk.Label(price_frame, text="Precio:",
                                           style="ProductInfoTitle.TLabel",
                                           anchor='w',
                                           justify='left')
        self.final_price_text.pack(side="left", padx=(0, 5))
        self.final_price_label = ttk.Label(price_frame, text=f"{discounted_price:.2f}€",
                                           style="ProductInfoText.TLabel",
                                           anchor='w',
                                           justify='left')
        self.final_price_label.pack(side="left", padx=(0, 5))

        self.discount_label = ttk.Label(price_frame, text=f"-{discount_percentage}%", style="ProductInfoHighlight.TLabel",
                                        anchor='w', justify='left')
        self.discount_label.pack(side="left", padx=(5, 5))

        self.original_price_label = ttk.Label(price_frame, text=f"{original_price:.2f}€",
                                              style="ProductInfoHighlight.TLabel", anchor='w', justify='left')
        self.original_price_label.pack(side="left", padx=(0, 5))
        self.original_price_label.configure(font=(self.original_price_label.cget("font"), 10, "overstrike"))

        # Especificaciones
        self.product_details_title = ttk.Label(info_frame, text="Especificaciones",
                                          style="ProductInfoTitle.TLabel",
                                          anchor='w',
                                          justify='left')
        self.product_details_title.pack(anchor='w', pady=(35, 5))
        self.product_details_frame = ttk.Frame(info_frame, style='ProductInfo.TFrame')
        self.product_details_frame.pack(anchor='w', pady=(0, 10))

        self.sku_weight_frame = ttk.Frame(self.product_details_frame, style='ProductInfo.TFrame')
        self.sku_weight_frame.pack(anchor='w', pady=(0, 10))

        self.weight_label = ttk.Label(self.sku_weight_frame, text=f"- Peso: {self.product.weight}",
                                      style="ProductAdditionalInfo.TLabel",
                                      anchor='w',
                                      justify='left')
        self.weight_label.pack(anchor='w', pady=(0, 5))

        self.sku_label = ttk.Label(self.sku_weight_frame, text=f"- SKU: {self.product.sku}",
                                   style="ProductAdditionalInfo.TLabel",
                                   anchor='w',
                                   justify='left')
        self.sku_label.pack(anchor='w', pady=(5, 0))

        self.dimensions_frame = ttk.Frame(self.product_details_frame, style='ProductInfo.TFrame')
        self.dimensions_frame.pack(anchor='w', pady=(0, 10))

        self.dimensions_label = ttk.Label(self.dimensions_frame, text="- Dimensiones:", style="ProductAdditionalInfo.TLabel",
                                          anchor='w', justify='left')
        self.dimensions_label.pack(anchor='w')

        self.height_label = ttk.Label(self.dimensions_frame, text=f"- Altura: {self.product.dimensions.height}", style="ProductInfoDimensions.TLabel", anchor='w',
                                      justify='left')
        self.height_label.pack(anchor='w', padx=(15, 10), pady=(0, 5))

        self.width_label = ttk.Label(self.dimensions_frame, text=f"- Ancho: {self.product.dimensions.width}", style="ProductInfoDimensions.TLabel", anchor='w',
                                     justify='left')
        self.width_label.pack(anchor='w', padx=(15, 10), pady=(0, 5))

        self.depth_label = ttk.Label(self.dimensions_frame, text=f"- Profundidad: {self.product.dimensions.depth}", style="ProductInfoDimensions.TLabel", anchor='w',
                                     justify='left')
        self.depth_label.pack(anchor='w', padx=(15, 10), pady=(0, 5))

        # Informacion extra
        self.extra_info_title = ttk.Label(info_frame, text="Información Extra",
                                          style="ProductInfoTitle.TLabel",
                                          anchor='w',
                                          justify='left')
        self.extra_info_title.pack(anchor='w', pady=(10, 5))
        self.extra_info_frame = ttk.Frame(info_frame, style='ProductInfo.TFrame')
        self.extra_info_frame.pack(anchor='w', pady=(0, 10))

        self.warranty_label = ttk.Label(self.extra_info_frame, text=f"Garantía: {self.product.warranty_information}", style="ProductAdditionalInfo.TLabel", anchor='w', justify='left')
        self.warranty_label.pack(anchor='w', pady=(0, 5))

        self.shipping_label = ttk.Label(self.extra_info_frame, text=f"Información de envío: {self.product.shipping_information}", style="ProductAdditionalInfo.TLabel", anchor='w', justify='left')
        self.shipping_label.pack(anchor='w', pady=(0, 5))

        self.availability_label = ttk.Label(self.extra_info_frame, text=f"Disponibilidad: {self.product.availability_status}", style="ProductAdditionalInfo.TLabel", anchor='w', justify='left')
        self.availability_label.pack(anchor='w', pady=(0, 5))

        # Subtitle para las Reviews
        self.reviews_subtitle = ttk.Label(self.product_info_frame, text="Reviews", style="Subtitle.TLabel", anchor='w', justify='left')
        self.reviews_subtitle.grid(row=2, column=0, columnspan=2, padx=(20, 20), pady=(20, 10), sticky='w')

        # Configurar layout general
        self.place(x=0, y=0, relwidth=1, relheight=1)

    def volver_atras(self):
        from views.main_screen import MainScreen
        self.controller.show_frame(MainScreen)

    def configure_scrollregion(self):
        self.product_info_canvas.configure(scrollregion=self.product_info_canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        canvas_height = event.height
        self.product_info_canvas.itemconfig(self.canvas_window, width=canvas_width, height=canvas_height)
