def calcular_desconto(valor_compra):
    if valor_compra > 500:
        desconto = 0.25  
    elif valor_compra > 200:
        desconto = 0.15  
    elif valor_compra > 100:
        desconto = 0.10 
    else:
        desconto = 0.00  
    
    valor_desconto = valor_compra * desconto
    valor_final = valor_compra - valor_desconto
    return valor_final, valor_desconto

valor_compra = float(input("Informe o valor da compra: R$"))

valor_final, valor_desconto = calcular_desconto(valor_compra)

print(f"Desconto aplicado: R${valor_desconto:.2f}")
print(f"Valor final da compra com desconto: R${valor_final:.2f}")
