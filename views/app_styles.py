from tkinter import ttk

from views.app_colors import AppColors


class AppStyles:
    @staticmethod
    def configure_styles(window_to_style):
        window_to_style.style = ttk.Style()
        window_to_style.style.theme_use('default')
        window_to_style.style.configure('TFrame',
                                        background=AppColors.main_bg)

        window_to_style.style.configure('Section.TFrame',
                                        background=AppColors.section_bg)

        # Estilos botones
        window_to_style.style.configure('TButton',
                                        font=('helvetica', '14'),
                                        background=AppColors.btn_bg,
                                        foreground=AppColors.btn_text,
                                        anchor="center",
                                        padding=10,
                                        relief="flat")

        window_to_style.style.map('TButton',
                                  foreground=[('pressed', AppColors.btn_pressed_text),
                                              ('active', AppColors.btn_hover_text)],
                                  background=[('pressed', AppColors.btn_pressed_bg),
                                              ('active', AppColors.btn_hover_bg)])

        # Estilo titulos
        window_to_style.style.configure('Title.TLabel',
                                        font=('helvetica', '20', "bold"),
                                        foreground=AppColors.title,
                                        background=AppColors.main_bg)

        # Estilo barra de busqueda
        window_to_style.style.configure('Search.TEntry',
                                        font=('helvetica', '14'),
                                        foreground=AppColors.entry_text,
                                        fieldbackground=AppColors.entry_bg,
                                        background=AppColors.entry_bg)

        # Estilos para ProductCard
        window_to_style.style.configure("ProductCard.TFrame",
                                        background= AppColors.product_card_bg,
                                        padding=10, relief="raised")
        window_to_style.style.configure("ProductCard.TLabel",
                                        background= AppColors.product_card_img_bg)
        window_to_style.style.configure("ProductCardTitle.TLabel",
                                        font=("Helvetica", 14, "bold"),
                                        foreground=AppColors.product_card_title,
                                        background=AppColors.product_card_bg)
        window_to_style.style.configure("ProductCardDesc.TLabel",
                                        font=("Helvetica", 10),
                                        foreground=AppColors.product_card_description,
                                        background=AppColors.product_card_bg)

        # ScrollBar
        window_to_style.style.configure("TScrollbar",
                                        background=AppColors.scrollbar_bg,
                                        troughcolor=AppColors.scrollbar_tg,
                                        bordercolor=AppColors.scrollbar_border,
                                        arrowcolor=AppColors.scrollbar_arrow)

        # Estilos para ProductInfo
        window_to_style.style.configure("ProductInfo.TFrame",
                                        background=AppColors.main_bg,
                                        padding=15)
        window_to_style.style.configure("ProductCategory.TLabel",
                                        font=('Helvetica', 18, 'bold', 'italic'),
                                        foreground=AppColors.important_text,
                                        background=AppColors.main_bg)
        window_to_style.style.configure("ProductInfoTitle.TLabel",
                                        font=('Helvetica', 16, 'bold'),
                                        foreground=AppColors.title,
                                        background=AppColors.main_bg)
        window_to_style.style.configure("ProductInfoText.TLabel",
                                        font=('Helvetica', 14),
                                        foreground=AppColors.text,
                                        background=AppColors.main_bg)
        window_to_style.style.configure("ProductInfoHighlight.TLabel",
                                        font=('Helvetica', 14, 'italic'),
                                        foreground=AppColors.link_text,
                                        background=AppColors.main_bg)
        window_to_style.style.configure("ProductReview.TLabel",
                                        font=('Helvetica', 12),
                                        foreground=AppColors.text,
                                        background=AppColors.main_bg)
        window_to_style.style.configure("ProductReviewRating.TLabel",
                                        font=('Helvetica', 12, 'bold'),
                                        foreground=AppColors.btn_pressed_text,
                                        background=AppColors.main_bg)
        window_to_style.style.configure("ProductAdditionalInfo.TLabel",
                                        font=('Helvetica', 13),
                                        foreground=AppColors.text,
                                        background=AppColors.main_bg)
        window_to_style.style.configure("ProductInfoImage.TLabel",
                                        background=AppColors.product_card_img_bg)
        window_to_style.style.configure("ProductInfoDimensions.TLabel",
                                        font=('Helvetica', 11),
                                        foreground=AppColors.text,
                                        background=AppColors.main_bg)

