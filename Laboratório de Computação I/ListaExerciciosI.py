def Q1_I() :
    n = int(input("Digite um número inteiro: "))
    divisores = []
    total = 0

    # Para todos os números abaixo no número informado, ele checa se é um
    # divisor
    # Se for ele insere na lista.
    for i in range(n - 1, 0, -1) :
        if n % i == 0 :
            divisores.append(i)

    # Ele então faz a soma de todos os divisores
    # E escreve na tela a soma com o resultado no final
    print("A soma é: ", end = "")
    for i in range(0, len(divisores)) :
        total += divisores[i]

        # Se chegou no final, ele escreve '=' e o resultado
        # Se não ele escreve um divisor com '+'
        if i == len(divisores) - 1 :
            print(str(divisores[i]) + " = " + str(total))
        else :
            print(divisores[i], end = " + ")
       
def Q2_I() :
    # Define uma entrada, uma matriz, e um iterador.
    entrada = input("Digite uma matriz numérica, linhas separadas por ';': ")
    matriz = [[]]
    j = 0

    # For para todo o tamanho da entrada.
    for i in range(len(entrada)) :
        # Tenta converter a entrada para um número inteiro.
        try :
            int(entrada[i])
            matriz[j].append(int(entrada[i]))
        # Se der erro, significa que chegou ao fim da linha ou é o caracter ';'.
        # Cria mais uma linha e aumenta o iterador.
        except :
            matriz.append([])
            j += 1

    # Por fim escreve a matriz.
    for i in range(len(matriz)) :
        print(matriz[i])
    
def Q3_I() :
    n = input("Digite o número de entradas da sequência de Fibonacci: ")
    x = 0
    y = 1
    z = 0

    # Escreve os valores
    for i in range(int(n)) :
        print(x, end = " ")
        z = x + y
        x = y
        y = z
        
def Q4_I() :
    frase = []
    fraseReversa = []
    contem = False
    entrada = input("Digite uma frase: ")
    # Adiciona um espaço no final da frase e remove as vírgulas
    entrada += " "
    entrada = entrada.replace(",", "")
    
    for i in range(len(entrada)) :
        # Se não for igual a uma espaço, adiciona o caractere as listas
        if entrada[i] != " ":
            frase.append(entrada[i].lower())
            fraseReversa.append(entrada[i].lower())
        # Se for igual a um espaço, reverte a lista fraseReversa
        # E então checa se as duas são iguais
        # Se forem existe um palíndromo
        # Se não, a palavra não é um palídromo
        else :
            fraseReversa.reverse()
            if frase == fraseReversa and len(frase) > 1 :
                contem = True
                print("".join(frase) + " é um palíndromo")
            frase.clear()
            fraseReversa.clear()

    if not contem : 
        print("A frase não contém nenhum palíndromo")

def Q5_I() :
    entrada = input("Digite uma lista de números: ")
    entrada = entrada.replace(" ", "")
    entrada += " "
    aux = ""
    lista = []
    lista2 = []

    for i in range(len(entrada)) :
        # Verifica se a entrada é numérica.
        # Se for adiciona o número em uma variável
        if entrada[i].isnumeric() :
            aux += entrada[i]
        # Se não for, insere o número nas listas e então o reseta
        elif aux.isnumeric() :
            lista.append(int(aux))
            lista2.append(int(aux))
            aux = ""

    # Itera sobre a lista2
    for i in range(len(lista2)) :
        # Se o valor na lista2 for ímpar remove da lista1
        if lista2[i] % 2 != 0 :
            lista.remove(lista2[i])
    
    # Escreve a lista1 reversa
    lista.reverse()
    print(lista)