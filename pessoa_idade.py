class Pessoa:
    __idade = 15
    __nome = "Carlos"
    
    def getIdade(self):
        return self.__idade
    
    def getNome(self):
        return self.__nome
#####################################
    
p1 = Pessoa()
minhaIdade = p1.getIdade()

novaIdade = p1.getIdade() + 1

print(f"Eu tenho {minhaIdade} anos e vou completar {novaIdade} anos.")
