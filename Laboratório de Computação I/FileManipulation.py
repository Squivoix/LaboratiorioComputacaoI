def FileManipulation() :
    with open("Arquivos/NomesCadastrados.txt", "w") as f :
        f.write("")

    file = open("Arquivos/NomesCadastrados.txt", "r+")
    data = file.read()

    cod = -1
    print("Códigos:\n1 - Cadastrar nomes.\n2 - Listar nomes.\n9 - Sair.\n")
    while True :
        cod = input("Digite o código: ")

        if cod == "1" :

            data += input("Digite um nome: ") + "\n"
            file.truncate(0)
            file.write(data)

        elif cod == "2" :

          if len(data) == 0 :
            print("\nLista vazia!\n")
          else :
            print("\n" + data)

        elif cod == "9" :
            print("Fechando programa!")
            file.close()
            break
        else :
            print("Código não existe!")
