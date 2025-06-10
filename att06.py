class Produto :
    def __init__(self, preco):
        self.__preco = preco
    def get_preco (self):
        return self.__preco
    def set_preco(self, preco):
        preco = float(preco)
        try:
            if preco>0:
                self.__preco = preco
                print("Novo preço adicionado com sucesso")
            else:
                print("preço negativo, tente novamente")
        except ValueError:
            print("Digite preço corretamente")


preco = input("Digite o seu Preço do produto ")

produto= Produto(preco)

novo_preço = input("Digite outro preço")

produto.set_preco(novo_preço)

print(Produto.get_preco())

