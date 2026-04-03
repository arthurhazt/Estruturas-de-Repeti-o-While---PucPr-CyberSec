while True:
    print("\n=== CALCULADORA ===")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo da calculadora...")
        break

    if opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print("Resultado:", num1 + num2)

        elif opcao == "2":
            print("Resultado:", num1 - num2)

        elif opcao == "3":
            print("Resultado:", num1 * num2)

        elif opcao == "4":
            if num2 == 0:
                print("Erro: divisão por zero!")
            else:
                print("Resultado:", num1 / num2)

    else:
        print("Opção inválida! Tente novamente.")