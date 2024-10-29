def classificar_palavras(palavras):
    curtas = []
    longas = []

    for palavra in palavras:
        if len(palavra) < 5:
            curtas.append(palavra)
        else:
            longas.append(palavra)

    return curtas, longas

def main():
    palavras_input = input("Insira palavras separadas por espaço: ")
    palavras = palavras_input.split()

    curtas, longas = classificar_palavras(palavras)

    print("\nPalavras curtas (menos de 5 letras):")
    print(", ".join(curtas) if curtas else "Nenhuma palavra curta.")

    print("\nPalavras longas (5 letras ou mais):")
    print(", ".join(longas) if longas else "Nenhuma palavra longa.")

if __name__ == "__main__":
    main()
