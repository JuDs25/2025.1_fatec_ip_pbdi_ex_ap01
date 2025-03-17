import calculadora

def menu():
    while True: # loop vai rodar indefinidamente. Para sair do loop, usamos um comando break
        print("\nMenu Operações Matemáticas: ")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        operacao = input("Escolha uma das opções das operações matemáticas, que consta no menu: ")
        if operacao == '0':
            print("Saindo...")
            break
        elif operacao in ['1', '2', '3', '4']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if operacao == "1":
                print(f"Resultado: {calculadora.somar(a, b)}")