class Pessoa:
    def __init__(self,nome_t, idade_t):
        self.nome = nome_t
        self.idade = idade_t
        
##########################################
p1 = Pessoa("João", 25)
print(p1.nome, p1.idade)
p1.email="joao@gmail.com" # incluir novo atributo
print(p1.email)

p2 = Pessoa("Ana", 31)
del(p2.idade) # excluir um atributo
print(p2.idade)

p3 = Pessoa("Carlos", 58)
print(p3.nome)
del(p3) # excluir objeto
print(p3.nome)
