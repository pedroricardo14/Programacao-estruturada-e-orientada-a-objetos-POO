class Inimigo:
    def __init__(self):
        self.nome = "Malvadão"
        self.__vida = 10
        
    def verVida(self):
        print(self.__vida)
    
    def menosVida(self):
        self.__vida -= 2
        if self.__vida <= 0:
            print("Morreu")
#######################
    
in1 = Inimigo()
print(in1.nome)
in1.verVida()
in1.menosVida()
in1.verVida()
in1.menosVida()
in1.verVida()
