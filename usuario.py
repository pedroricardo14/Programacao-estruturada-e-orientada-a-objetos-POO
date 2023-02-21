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
senha = input("Senha: ")
user1 = Usuario("João", "123")
user1.validar("456")
