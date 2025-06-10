class Aluno :
    def __init__(self, nome, nota ):

        self.__nome = nome 
        self.__nota = nota
    
    def get_nome(self):
        return self.__nome
    def get_nota(self):
        return self.__nota
    
    def set_nome(self, nome):
        nome = str(nome)
        if isinstance(nome, str)  and len(nome) >0:
            print("Nome mudado com sucesso")
            self.__nome= nome
        else:
            print("digite um nome valido")
    def set_nota(self, nota):
        try:
            nota = float(nota)
            if nota >= 0 and nota <= 10:
                print("Nota mudada com sucesso")
                self.__nota = nota
            else:
                print("Digite uma nota valida")
        except ValueError:
            print("Digite uma nota valida, apenas numeros")

nome = input("Qual o seu nome? ")

nota= input("Qual a sua nota? ")

aluno = Aluno(nome, nota)


nova_nota = input("Digite a sua nota novamente !!")
nova_nome = input("Digite o seu nome novamente !!")

aluno.set_nota(nova_nota)
aluno.set_nome(nova_nome)

print("Nome do aluno: ", aluno.get_nome())
print("Nota do aluno: ", aluno.get_nota())
