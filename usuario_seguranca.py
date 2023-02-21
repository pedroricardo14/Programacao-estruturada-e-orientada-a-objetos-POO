import getpass
class Usuario:
    def __init__(self, nome_t, senha_t):
        self.nome = nome_t		# public
        self.__senha = senha_t  # private
# Quando o self senha tem dois underlines antes, torna-se privada, ou seja, ninguém pode ver.

    def validar(self, senha_t):
        if senha_t == self.__senha:
            print("Acesso permitido")
        else:
            print("Acesso negado.")
##########################################
nome = input("Nome: ")
senha = getpass(prompt="Senha: ")
user1 = Usuario(nome, senha)
user1.validar("456")
