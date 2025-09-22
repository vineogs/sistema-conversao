import tkinter as tk
from frames.imagens import ImagensFrame
from frames.videos import VideosFrame
from frames.documentos import DocumentosFrame
from frames.csv import CsvFrame

def mostrat_sessao(sessao):
    for f in [frame_imagens, frame_videos, frame_documentos, frame_csv]:
        f.pack_forget()
    sessao.pack(fill="both", expand=True)

root = tk.Tk()
root.title("Exemplo de Frames")
root.geometry("800x400")

# HEADER
frame_top = tk.Frame(root, height=50)
frame_top.pack(side="top", fill="x")
tk.Label(frame_top, text="Conversor Multimídia", font=("Arial", 14)).pack(pady=10)

# ASIDE
frame_left = tk.Frame(root, width=150)
frame_left.pack(side="left", fill="y")
tk.Label(frame_left, text="Menu").pack(pady=10)

# CONTEÚDO CENTRAL
frame_center = tk.Frame(root, bg="lightgray")
frame_center.pack(side="right", fill="both", expand=True)

# Instanciando frames das sessões
frame_imagens = ImagensFrame(frame_center)
frame_videos = VideosFrame(frame_center)
frame_documentos = DocumentosFrame(frame_center)
frame_csv = CsvFrame(frame_center)

tk.Button(frame_left, text="Imagens", width=10, height=2, command=lambda: mostrat_sessao(frame_imagens)).pack(pady=5)
tk.Button(frame_left, text="Videos", width=10, height=2, command=lambda: mostrat_sessao(frame_videos)).pack(pady=5)
tk.Button(frame_left, text="Documentos", width=10, height=2, command=lambda: mostrat_sessao(frame_documentos)).pack(pady=5)
tk.Button(frame_left, text="CSV->SQL", width=10, height=2, command=lambda: mostrat_sessao(frame_csv)).pack(pady=5)

mostrat_sessao(frame_imagens)

root.mainloop()
