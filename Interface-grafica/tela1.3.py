from tkinter import *
janela = Tk()
rotulo = Label(janela,text="Olá, mundo!")
rotulo.grid(row=0, column=0)

pergunta = Label(janela, text="Tudo bem?")
#pergunta.grid(row=0, column=1)
#pergunta.grid(row=1, column=0)
pergunta.grid(row=1, column=1)
janela.mainloop()
