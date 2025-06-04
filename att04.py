class Conta_Bancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def mostrar_saldo(self):
        print(f"O seu saldo é {self.__saldo}")
    
    def saque(self, saldo):
        
        valor_saque = float(self.__saldo)
        if valor_saque <= self.__saldo:
            self.__saldo-= valor_saque
            print(f"O saque de R${valor_saque} foi realizado com sucesso")
            self.mostrar_saldo()
        else:
            print("Saldo Insuficiente!!")
            self.mostrar_saldo()
            
    def deposito(self):
        valor_deposito = float(self.__saldo)
        
        self.__saldo+=valor_deposito 
        print(f"O seu depostio de R$ {valor_deposito}, foi efetuado com sucesso!!")
        self.mostrar_saldo()
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        if isinstance(saldo, float) and saldo >0:
            self.__saldo = saldo
        else:
            print("Valor invalido")
                    

saldo_inicial = input("Qual o saldo da sua conta ? ")
conta = Conta_Bancaria(saldo_inicial)

escolha = input("Deseja fazer uma retirada ou depósito? ").strip().lower()

if escolha == 'retirada':
    valor_retirada = input("Qual o valor da sua retirada? ")
    conta.saque(valor_retirada)

elif escolha == 'depósito' or escolha == 'deposito':
    valor_deposito = input("Qual o valor do seu depósito? ")
    conta.deposito(valor_deposito)

else:
    print("Opção inválida.")
