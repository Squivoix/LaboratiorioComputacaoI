def Q1_II() :
    A = []
    B = []

    A.append(int(input("Digite a coordenada X do ponto A: ")))
    A.append(int(input("Digite a coordenada Y do ponto A: ")))
    
    B.append(int(input("Digite a coordenada X do ponto B: ")))
    B.append(int(input("Digite a coordenada Y do ponto B: ")))

    a = (A[0] - A[1]) ** 2
    b = (B[0] - B[1]) ** 2

    Resposta = (a + b) ** 0.5

    print("O resultado é", Resposta)

def Q2_II() :
    frase = input("Digite uma frase: ")
    palavrasEncontradas = []
    duplicatas = []

    palavrasEncontradas = frase.split(" ")

    for s in palavrasEncontradas :
        existe = False
        for i in range(0, len(duplicatas)) :
            if s.lower() == duplicatas[i][0] :
                duplicatas[i][1] += 1
                existe = True
                break
        
        if not existe :
            duplicatas.append([s.lower(), 1])

    for s in duplicatas :
        print(s[0] + ": ", end="")
        print(s[1])



def Q3_II() :
    A = []
    B = []
    num = ""

    frase1 = input("Digite a primeira lista de números inteiros, separados por vírgula: ")
    frase2 = input("Digite a segunda lista de números inteiros, separados por vírgula: ")

    A = frase1.split(",")
    B = frase2.split(",")

    B.reverse()
    print("\n")

    for i in range(0, len(A)) :
        print(str(A[i]) + "\t" + str(B[i]))

def Q4_II() :
    for i in range(0, 9) :
        if i < 5 :
            for i in range(0, i + 1) :
                print("*", end="")
        else :
            for i in range(0, 9 - i) :
                print("*", end="")
        
        print("\n")

def Q5_II() :
    lista = []
    soma = 0

    frase = input("Digite uma lista de números inteiros, separados por vírgula: ")

    lista = frase.split(",")
    lista = list(map(int, lista))

    for i in range(0, len(lista)) :
        if lista[i] % 3 == 0 or lista[i] % 5 == 0 :
            soma += lista[i]

            if i != len(lista) - 1 :
                print(str(lista[i]) + " + ", end="")
            else :
                print(str(lista[i]) + " = " + str(soma))
