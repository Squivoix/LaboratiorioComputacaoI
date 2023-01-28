def RepeatingLoops() :
    for i in range(1, 51, 2) :
        print(i)

def ReadingLoops() :
    lista = []
    s = ""
    n = 0.0

    print("Digite 'Sair' para sair do programa!")
    while True : 
        s = input("Digite um número: ")

        if s.capitalize() == "Sair" : 
            break

        try :
            n = float(s)
            lista.append(n)
        except :
            print("Por favor, digite um número!")

    lista.reverse()

    for valor in lista : 
        print(valor)