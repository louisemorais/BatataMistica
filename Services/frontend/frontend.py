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

try:
    bg_img = Image.open("../../assets/space.jpg").resize((largura_janela, altura_janela))
    bg_photo = ImageTk.PhotoImage(bg_img)
    canvas = Canvas(janela, width=largura_janela, height=altura_janela)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor=NW)

    # Carregar e centralizar a batata
    potato_img = Image.open("../../assets/potato.png")
    potato_photo = ImageTk.PhotoImage(potato_img)
    potato_w, potato_h = potato_img.size
    x_centro = (largura_janela - potato_w) // 2
    y_centro = (altura_janela - potato_h) // 2
    canvas.create_image(x_centro, y_centro, image=potato_photo, anchor=NW)
except:
    bg_img = Image.open("assets/space.jpg").resize((largura_janela, altura_janela))
    bg_photo = ImageTk.PhotoImage(bg_img)
    canvas = Canvas(janela, width=largura_janela, height=altura_janela)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor=NW)

    # Carregar e centralizar a batata
    potato_img = Image.open("assets/potato.png")
    potato_photo = ImageTk.PhotoImage(potato_img)
    potato_w, potato_h = potato_img.size
    x_centro = (largura_janela - potato_w) // 2
    y_centro = (altura_janela - potato_h) // 2
    canvas.create_image(x_centro, y_centro, image=potato_photo, anchor=NW)

janela.mainloop()
