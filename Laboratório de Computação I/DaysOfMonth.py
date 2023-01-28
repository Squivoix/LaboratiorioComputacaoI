def DaysOfMonth() :
    # Um porém é que dicionários não permitem duas entradas, ou seja, não se pode colocar duas Segundas, nem duas Terças
    Days = {}

    semana = ""
    dia = 0

    print("Escreva 'sair' ou 'Sair' para sair do programa!")

    while True :
        semana = input("\nEscreva o dia da semana: ")

        if semana.capitalize() == "Sair" :
            print("\n")
            break

        dia = input("Escreva o dia do mês: ")

        Days[semana] = dia

    for x in Days :
        if x.capitalize() == "Sábado" or x.capitalize() == "Sabado" or x.capitalize() == "Domingo" :
            print(x.capitalize() + " é dia " + str(Days[x]))
        else :
            print(x.capitalize() + " feira é dia " + str(Days[x]))
