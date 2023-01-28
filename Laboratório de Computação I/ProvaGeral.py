def Q1_G() :
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))

    cont = 0
    s = 0

    while cont < y :
        s += x
        cont += 1

    print('Resultado:', s)

def Q2_G() :
    nomeCompleto = "Lorem Ipsum"

    nome, sobrenome = nomeCompleto.split()

    if len(nome) > 4:
        print(sobrenome, nome)
    else: 
        print (nome, sobrenome)

def Q3_G() :
    def calcDias(mes) :
        dias = 31

        if mes == 2: dias = 28
        elif mes == 4: dias = 30
        elif mes == 6: dias = 30
        elif mes == 9: dias = 30
        elif mes == 11: dias = 30
        return dias

    mes = int(input("Informe o mês: "))
    resposta = calcDias(mes) 
    print("O mes", mes, "possui", resposta, "dias.")

def Q4_G() :
    def processar(x) :
        s = 0

        for i in range(x) :
            s += i + 1

        return s

    #parte principal
    N = int(input("Digite um número: "))
    saida = processar(N)
    print(saida)

def Q5_G() :
    slogan = "Copa do Mundo FIFA 2018"

    print("Bem vindo a " + slogan[0:4] + " " + slogan[19:23] + "!#" + slogan[14:18])

def Q6_G() :
    def soma(a, b) :
        s = 0

        while a < b :
            if s == 5 :
                continue
            s += a
            a += 1
            
        return s

    print(soma(2, 8))

def Q7_G() :
    lista = []
    seq = input("Digite uma sequência de números, separados por vírgula: ")
    s = 1

    lista = seq.split(",")
    lista = list(map(int, lista))

    for n in lista :
        if n != 0 :
            s *= n

    print(s)

def Q8_G() :
    fulano = 170
    ful_cres = 2
    cicrano = 150
    cic_cres = 4
    cont = 1

    while fulano != cicrano :
        fulano += ful_cres
        cicrano += cic_cres
        cont += 1

    print("Será necessário", cont, "anos para que Cicrano seja maior que Fulano!")

def Q9_G() :
    def VerificarPrimo(n) :
        for i in range(1, n) : # Verifica todos os números desde '1' até 'n'
            if i != 1 and i != n and n % i == 0 :
                return False

        return True

    lista = []

    for i in range(3) :
        lista.append(int(input("Digite um número: ")))

    for n in lista :
        if VerificarPrimo(n) :
            print(n, "é primo!")
        else :
            print(n, "não é primo!")

def Q10_G() :
    cod = 0
    print("Códigos:\n1 - Gravar Nome e CPF.\n2 - Mostrar todos os Nomes e CPFs.\n9 - Sair.")

    while cod != "9" :
        cod = input("\nDigite um código: ")
        data = ""

        if cod == "1" : # Gravar Nome e CPF.
            data += "Nome: " + input("Digite um Nome: ")
            data += ", CPF: " + input("Digite um CPF: ") + "\n"

            file = open("Arquivos/DadosCadastrados.txt", "a")
            file.write(data)
            file.close()
        elif cod == "2" : # Mostrar todos os Nomes e CPFs.
          file = open("Arquivos/DadosCadastrados.txt", "r")
          data = file.read()

          if len(data) == 0 :
            print("\nLista vazia!")
          else :
            print("\n" + data)
        
            file.close()
        elif cod == "9" :
            print("\nSaindo do Programa!")
        else :
            print("\nCódigo não existe!")


def Q11_G() :
    a = int(input("Digite o primeiro lado de um triângulo: "))
    b = int(input("Digite o segundo lado de um triângulo: "))
    c = int(input("Digite o terceiro lado de um triângulo: "))

    if a == b == c : # Três lados iguais
        print("O triângulo é equilátero!")
    elif (a == b != c) or (a != b == c) or (a == c != b) : # Dois lados iguais
        print("O triângulo é isóceles!")
    elif a != b != c : # Três lados diferentes
        print("O triângulo é escaleno!")