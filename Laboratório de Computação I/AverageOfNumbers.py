lista = []

def AumentarValores() :
    positivos = 0
    divPos = 0
    negativos = 0
    divNeg = 0

    for j in lista :
        if j < 0 :
            negativos += j
            divNeg += 1
        elif j > 0 :
            positivos += j
            divPos += 1

    negativos /= divNeg
    positivos /= divPos

    print("\nA média dos números positivos é", positivos)
    print("A média dos números negativos é", negativos)

def AverageOfNumbers() :
    for i in range(0, 10) :
        lista.append(int(input("Digite um número inteiro: ")))
    
    AumentarValores()

