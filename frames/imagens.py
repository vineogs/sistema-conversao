import tkinter as tk

class ImagensFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="pink")
        tk.Label(self, text="Sessão Imagens", bg="pink", font=("Arial", 12)).pack(pady=20)
        # Aqui você pode adicionar mais widgets específicos dessa sessão
