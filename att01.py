class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome) >0:
            self.__nome = nome
        else:
            print("Nome invalido")
            

nome = input("Digite  seu nome ")

pessoa = Pessoa(nome)

print(pessoa.get_nome())
