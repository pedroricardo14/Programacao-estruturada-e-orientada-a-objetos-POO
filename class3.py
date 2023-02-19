class Pessoa:
    #nome = ""						#Nessa parte tanto faz colocar essas variáveis aqui ou não
    #idade = ""
    
    def __init__(self, pnome, pidade):
        self.nome = pnome
        self.idade = pidade
###############################################
        
#p1 = Pessoa()  # dá erro
        
p1 = Pessoa("Camila", 26)
p2 = Pessoa("Kaio", 19)

nome3 = input("Digite o nome: ")
idade3 = input("Digite a idade: ")
p3 = Pessoa(nome3, idade3)

print(f"{p3.nome} tem {p3.idade} anos.")
