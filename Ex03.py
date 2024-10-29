def combinar_nomes(nome1, nome2):
    metade1 = nome1[:len(nome1)//2]  
    metade2 = nome2[len(nome2)//2:] 
    
    nome_combinado = metade1 + metade2
    
    return nome_combinado.capitalize()

nome1 = input("Digite o primeiro nome de usuário: ")
nome2 = input("Digite o segundo nome de usuário: ")

nome_combinado = combinar_nomes(nome1, nome2)

print(f"O novo nome criativo é: {nome_combinado}")
