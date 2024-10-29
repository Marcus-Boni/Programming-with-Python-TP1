import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Adivinhe o número secreto (entre 1 e 100): "))

    if palpite == numero_secreto:
        print("Parabéns! Você adivinhou o número secreto.")
        break
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Muito baixo! Tente novamente.")
