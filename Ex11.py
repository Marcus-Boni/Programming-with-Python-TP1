import random

def lancar_dados(num_dados):
    resultados = []
    for _ in range(num_dados):
        resultados.append(random.randint(1, 6))
    return resultados

def main():
    try:
        num_dados = int(input("Quantos dados você deseja lançar? "))
        if num_dados <= 0:
            print("Por favor, insira um número positivo.")
            return
        
        resultados = lancar_dados(num_dados)
        print(f"Resultados dos lançamentos: {resultados}")
        
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
