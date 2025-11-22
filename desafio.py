while True:   # MENU PRINCIPAL
    print("\nEscolha qual desafio deseja testar digitando um número de 1 a 6:")
    desafio = input("> ")

    # Verifica se é número
    if not desafio.isdigit():
        print("❌ Entrada inválida! Digite apenas números de 1 a 6.")
        continue

    desafio = int(desafio)

    # Verifica intervalo
    if not (1 <= desafio <= 6):
        print("❌ Número fora do intervalo! Digite um número de 1 a 6.")
        continue


    # ------------------ DESAFIO 1 ------------------
    if desafio == 1:
        print("\n1️⃣ Desafio 1 - Concatenando Dados 🐾")
        dado1 = input("Digite o primeiro dado: ")
        dado2 = input("Digite o segundo dado: ")
        print("\nResultado:", dado1 + dado2)


    # ------------------ DESAFIO 2 ------------------
    elif desafio == 2:
        print("\n2️⃣ Desafio 2 - Repetindo Textos ✏️")

        frase = input("Digite a frase: ")

        vezes = input("Digite quantas vezes repetir: ")
        if not vezes.isdigit():
            print("❌ Entrada inválida! Digite apenas números.")
            continue

        vezes = int(vezes)

        while vezes > 0:
            print(frase)
            vezes -= 1


    # ------------------ DESAFIO 3 ------------------
    elif desafio == 3:
        print("\n3️⃣ Desafio 3 - Operações Matemáticas Simples 📐")

        num1 = input("Digite o primeiro número: ")
        if not num1.isdigit():
            print("❌ Entrada inválida! Digite apenas números.")
            continue
        num1 = int(num1)

        num2 = input("Digite o segundo número: ")
        if not num2.isdigit():
            print("❌ Entrada inválida! Digite apenas números.")
            continue
        num2 = int(num2)

        print(f"✔ Resultado da soma: {num1 + num2}")


    # ------------------ DESAFIO 4 ------------------
    elif desafio == 4:
        print("\n4️⃣ Desafio 4 - Verificando Números Pares e Ímpares 🧮")
        num = input("Digite um número inteiro: ")

        if not num.isdigit():
            print("❌ Entrada inválida! Digite apenas números.")
            continue

        num = int(num)

        if num % 2 == 0:
            print(f"✔ O número {num} é PAR")
        else:
            print(f"✔ O número {num} é ÍMPAR")


    # ------------------ DESAFIO 5 ------------------
    elif desafio == 5:
        print("\n5️⃣ Desafio 5 - Calculando Média de Notas 📚")

        notas = []

        for i in range(1, 4):
            nota = input(f"Digite a {i}ª nota: ")

            if not nota.isdigit():
                print("❌ Entrada inválida! Digite apenas números.")
                break

            notas.append(int(nota))

        else:
            media = sum(notas) / 3
            print(f"✔ A média das notas é: {media:.2f}")


    # ------------------ DESAFIO 6 ------------------
    elif desafio == 6:
        print("\n6️⃣ Desafio 6 - Verificando Palíndromos 🔄")

        palavra = input("Digite uma palavra: ").strip().lower()
        invertida = palavra[::-1]

        if palavra == invertida:
            print(f"✔ '{palavra}' é um palíndromo!")
        else:
            print(f"❌ '{palavra}' não é um palíndromo.")


    print("\n✔ Desafio finalizado! Reiniciando menu...")
