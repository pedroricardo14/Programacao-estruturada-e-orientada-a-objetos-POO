from tkinter import *
janela = Tk()
texto1 = "Esse é\num texto\ncom várias\nlinhas."
rot1 = Label(janela, text = texto1, justify="left")
rot1.grid(row=0, column=0)
texto2 = """Esse texto
também tem
várias linhas."""
rot2 = Label(janela, text = texto2, justify="right")
rot2.grid(row=1, column=1)

imagem = PhotoImage(file="if.png")
rot3 = Label(janela, image = imagem)
rot3.grid(row=2,column=2)
janela.mainloop()
