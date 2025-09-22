import tkinter as tk

class DocumentosFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightgreen")
        tk.Label(self, text="Sessão Documentos", bg="lightgreen", font=("Arial", 12)).pack(pady=20)
