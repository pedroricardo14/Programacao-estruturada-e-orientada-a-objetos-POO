import math

class Circulo:
    raio = 0
    
    def __init__(self, r):
        if < 0:
            self.raio = r * - 1 # inverte o sinal
        else: self.raio = r
        
    def diametro(self):
        print(f"Diâmetro = {2 * self.raio}")
        
    def area(self):
        print(f"Área = {math.pi * self.raio ** 2}")
        
    def circunferencia(self):
        print(f"Circunferência = {2 * math.pi * self.raio}")
        
    def info(self):
        print(f"Raio = {self.raio}")
        
############################################################
        
circ_peq = Circulo(2)
circ_peq.diametro()
circ_peq.area()
circ_peq.circunferencia()
circ_peq.info()
        
