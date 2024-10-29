def main():
    opcoes = {
        'Opção 1': 0,
        'Opção 2': 0,
        'Opção 3': 0
    }

    print("Vote em uma das três opções:")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("0 - Finalizar votação")

    while True:
        try:
            voto = int(input("Digite o número da sua opção: "))

            if voto == 0:
                break
            elif voto == 1:
                opcoes['Opção 1'] += 1
            elif voto == 2:
                opcoes['Opção 2'] += 1
            elif voto == 3:
                opcoes['Opção 3'] += 1
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Por favor, insira um número válido.")

    print("\nResultados da votação:")
    for opcao, votos in opcoes.items():
        print(f"{opcao}: {votos} voto(s)")

if __name__ == "__main__":
    main()
