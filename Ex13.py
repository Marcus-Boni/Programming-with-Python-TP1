def eh_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

def main():
    frase = input("Insira uma palavra ou frase: ")
    
    if eh_palindromo(frase):
        print(f'"{frase}" é um palíndromo.')
    else:
        print(f'"{frase}" não é um palíndromo.')

if __name__ == "__main__":
    main()
