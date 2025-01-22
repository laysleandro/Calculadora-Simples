def menu():
    print("=== CALCULADORA SIMPLES ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print("===========================")

def calculadora():
    while True:
        menu()
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '5':
            print("Encerrando a calculadora. Até logo!")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar números.")
            continue

        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif escolha == '4':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida!")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                
calculadora()
