def historia():
    print("Você está em uma floresta misteriosa.")
    print("Você vê um caminho à sua frente e uma caverna à sua direita.")
    print("1 - Seguir o caminho")
    print("2 - Entrar na caverna")
    
    escolha1 = input("Faça sua escolha (1 ou 2): ")
    
    if escolha1 == '1':
        print("\nVocê segue o caminho e encontra um lago encantado.")
        print("Você pode:")
        print("1 - Beber da água")
        print("2 - Continuar caminhando")
        
        escolha2 = input("Faça sua escolha (1 ou 2): ")
        
        if escolha2 == '1':
            print("\nVocê se sente rejuvenescido e descobre que pode voar!")
            print("Você voa para longe e vive uma vida cheia de aventuras.")
        elif escolha2 == '2':
            print("\nVocê continua caminhando e encontra uma cidade mágica.")
            print("Na cidade, você se torna um grande mago e é respeitado por todos.")
        else:
            print("\nEscolha inválida. O destino da sua jornada é incerto.")
    
    elif escolha1 == '2':
        print("\nVocê entra na caverna e encontra um tesouro escondido.")
        print("Você pode:")
        print("1 - Pegar o tesouro")
        print("2 - Deixar o tesouro e sair")
        
        escolha2 = input("Faça sua escolha (1 ou 2): ")
        
        if escolha2 == '1':
            print("\nVocê pega o tesouro e se torna rico!")
            print("Mas cuidado, você acordou um dragão!")
            print("Você deve enfrentar o dragão para escapar.")
        elif escolha2 == '2':
            print("\nVocê deixa o tesouro e sai da caverna.")
            print("Você se sente em paz e decide viver uma vida simples.")
        else:
            print("\nEscolha inválida. A caverna permanece um mistério.")
    
    else:
        print("\nEscolha inválida. Sua aventura termina aqui.")

if __name__ == "__main__":
    historia()
