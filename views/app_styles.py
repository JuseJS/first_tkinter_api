from tkinter import ttk


class AppStyles:
    def __init__(self, window_to_style):

        window_to_style.style = ttk.Style()
        window_to_style.style.theme_use('default')
        window_to_style.style.configure('TFrame', background='#1C1C1E')

        # Estilo titulos
        window_to_style.style.configure('Title.TLabel',
                                        font=('helvetica', '20', "bold"),
                                        foreground='#FFFFFF',
                                        background='#1C1C1E')
        # Estilo barra de busqueda
        window_to_style.style.configure('Search.TEntry',
                                        font=('helvetica', '14'),
                                        foreground='#E5E5E5',
                                        fieldbackground='#4A4A4A',
                                        background='#333333')