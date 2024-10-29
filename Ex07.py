def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informe a sua altura em metros (ex: 1.75): "))

imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está com peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
