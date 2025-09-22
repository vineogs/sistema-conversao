import tkinter as tk

class VideosFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue")
        tk.Label(self, text="Sessão Vídeos", bg="lightblue", font=("Arial", 12)).pack(pady=20)
