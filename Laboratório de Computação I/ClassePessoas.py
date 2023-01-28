class Pessoa:

    def Cadastrar(self):
        print('Cadastro de dados de uma Pessoa')
        
        self.nome = input('\nDigite seu Nome: ')
        self.sobrenome = input('Digite seu Sobrenome: ')
        self.idade = input('Digite sua idade: ')

    def Mostrar(self):
        print('#'*10)
        print(f'Nome: {self.nome}')
        print(f'Sobrenome: {self.sobrenome}')
        print(f'Idade: {self.idade}')
        print('#'*10)

#parte principal
def ClassePessoas() :
    pessoa1 = Pessoa()
    pessoa1.Cadastrar()

    pessoa2 = Pessoa()
    pessoa2.Cadastrar()

    pessoa1.Mostrar()
    pessoa2.Mostrar()
