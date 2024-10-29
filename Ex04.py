def calcular(operacao, num1, num2):
    if operacao == '1':
        return num1 + num2
    elif operacao == '2':
        return num1 - num2
    elif operacao == '3':
        return num1 * num2
    elif operacao == '4':
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        return num1 / num2
    else:
        return "Operação inválida."

print("Escolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação desejada: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = calcular(operacao, num1, num2)

print(f"O resultado da operação é: {resultado}")
