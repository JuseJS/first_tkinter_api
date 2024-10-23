import tkinter as tk

from views.main_screen import MainScreen


class MainApp(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(size)

        self.container = tk.Frame(self, height=1600, width=800)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.show_frame(MainScreen)

        self.mainloop()

    def show_frame(self, cont, *args, **kwargs):
        if cont not in self.frames:
            frame = cont(self.container, self, *args, **kwargs)
            self.frames[cont] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        frame = self.frames[cont]
        frame.tkraise()
