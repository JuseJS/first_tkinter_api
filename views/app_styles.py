from tkinter import ttk


class AppStyles:
    def __init__(self, window_to_style):

        window_to_style.style = ttk.Style()
        window_to_style.style.theme_use('default')
        window_to_style.style.configure('TFrame',
                                        font=('helvetica', '12'),
                                        foreground='#E5E5E5',
                                        background='#1C1C1E')