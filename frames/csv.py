import tkinter as tk

class CsvFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        tk.Label(self, text="Sessão CSV -> Insert SQL", bg="white", font=("Arial", 12)).pack(pady=20)
