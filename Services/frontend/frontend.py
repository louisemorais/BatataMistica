from tkinter import *
from PIL import Image, ImageTk

janela= Tk()
janela.title("batata mística")

largura_janela = 800
altura_janela = 600

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


background =ImageTk.PhotoImage(Image.open("space.jpg"))
batata=ImageTk.PhotoImage(Image.open(file="potato.png"))

Label(janela,image=background)


janela.mainloop()


