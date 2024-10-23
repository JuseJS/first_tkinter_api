from tkinter import ttk

from views.app_styles import AppStyles


class ProductScreen(ttk.Frame):
        # self.parent_name = parent.winfo_parent()
        # self.parent = parent.nametowidget(self.parent_name)
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.product = args[1]

        # Cargamos los estilos
        AppStyles.configure_styles(self)

        # Frame principal de la ventana
        self.main_frame = ttk.Frame(self, style='TFrame')
        self.main_frame.pack(expand=True, fill="both")

        # Titulo de la ventana
        self.title = ttk.Label(self.main_frame, text=self.product.title, style="Title.TLabel", anchor="e", justify="center")
        self.title.place(x=0, y=20, width=850)

        # Barra de busqueda
        self.search_entry = ttk.Entry(self.main_frame, style="Search.TEntry")
        self.search_entry.place(x=1250, y=20, width=300, height=30)

        btn = ttk.Button(text="Volver Atras", command=self.volver_atras)
        btn.pack()

        self.place(x=0, y=0, relwidth=1, relheight=1)

    def volver_atras(self):
        self.main_frame.destroy()