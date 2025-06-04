class Carro :
    def __init__(self, modelo):
        self.__modelo =modelo
        
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        if isinstance(modelo, str) and len(modelo) >0:
            self.__modelo = modelo
        else:
            print("Modelo invalido")


modelo = input("Qual o modelo do seu carro ")

carro = Carro(modelo)

novo_modelo= input("Digite novemente")

carro.set_modelo(novo_modelo)


