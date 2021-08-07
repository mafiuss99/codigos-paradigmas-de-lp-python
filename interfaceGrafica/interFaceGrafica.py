from tkinter import *

def funcClicar():
    print("Botão presionado")

janelaPrincipal=Tk()

texto=Label(master=janelaPrincipal, text="Minha janela exibida")
texto.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()