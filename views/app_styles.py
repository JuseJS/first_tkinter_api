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
