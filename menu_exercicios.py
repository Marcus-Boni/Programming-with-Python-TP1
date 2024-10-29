import os
import subprocess
import platform

negrito = "\033[1m"
reset = "\033[0m"
verde = "\033[92m"
cinza = "\033[90m"
vermelho = "\033[91m"
azul = "\033[94m"
amarelo = "\033[93m"
arquivo_emoticon = "📄"
pasta_emoticon = "📁"
voltar_emoticon = "🔙"
refresh_emoticon = "🔄"
check_emoticon = "✔️"
sair_emoticon = "👋"
barra_concluida = "■"
barra_pendente = "□"
cancelar_emoticon = "❌"
alerta_emoticon = "⚠️"

def listar_exercicios():
    exercicios = []
    # Caminha apenas pela pasta onde o arquivo atual está localizado
    pasta_atual = os.path.dirname(__file__)
    for f in os.listdir(pasta_atual):
        if f.startswith("Ex") and f.endswith(".py") and f != os.path.basename(__file__):
            caminho_completo = os.path.join(pasta_atual, f)
            exercicios.append(caminho_completo)

    # Ordena os arquivos encontrados por número, se houver número no nome
    exercicios = sorted(
        exercicios, 
        key=lambda x: int(os.path.basename(x)[2:-3]) if os.path.basename(x)[2:-3].isdigit() else 0
    )
    
    return exercicios

def limpar_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def exibir_menu():
    executados = set()  # Armazena os índices dos exercícios já executados
    
    while True:
        limpar_tela()
        print(f"{cinza}===[{reset}{azul} Menu de Exercícios {cinza}] • [{reset}{azul} by André Luis Becker {cinza}] • [{reset}{azul} Todos os direitos reservados {reset}{cinza}]==={reset}\n")
        
        exercicios = listar_exercicios()
        
        if not exercicios:
            print(f"{cinza}{alerta_emoticon} Nenhum exercício encontrado na pasta atual!{reset}")
            break

        # Cabeçalho da tabela
        print(f"{cinza}{'-'*90}{reset}")
        print(f"{negrito}    Nº   {arquivo_emoticon} Arquivo                   {pasta_emoticon} Pasta{reset}")
        print(f"{cinza}{'-'*90}{reset}")
        
        for indice, caminho_exercicio in enumerate(exercicios, start=1):
            nome_exercicio = os.path.basename(caminho_exercicio)
            diretorio = os.path.dirname(caminho_exercicio)
            numero_formatado = f"{cinza}[{verde}{negrito}{indice:2}{reset}{cinza}]{reset}"
            estado = f"{check_emoticon}{reset}" if indice in executados else " " * len(check_emoticon)  # Marca exercícios já executados

            print(f"{estado} {numero_formatado}  {arquivo_emoticon} {nome_exercicio:<25} {pasta_emoticon} {cinza}{diretorio}{reset}")
            print("")

        while True:
            print(f"{cinza}{'-'*90}{reset}")
            print(f"{azul}{refresh_emoticon} [A] Atualizar{reset}          {vermelho}{cancelar_emoticon} [0] Sair{reset}")
            print(f"{cinza}{'-'*90}{reset}")
            escolha = input(f"{negrito}\nPara executar digite o {verde}Nº {reset}{negrito}do exercício: {reset}{verde}")
            
            if escolha == '0':
                print(f"\n{amarelo}{sair_emoticon} Saindo do programa. Até logo!{reset}")
                return
            
            if escolha.strip().lower() == 'a':
                break  # Sai do loop de escolha e reinicia o menu
            
            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(exercicios):
                    caminho_exercicio = exercicios[indice]
                    executados.add(indice + 1)  # Adiciona o índice à lista de exercícios executados

                    # Exibe o cabeçalho de execução
                    print(f"\n{azul}{negrito}--- Executando {os.path.basename(caminho_exercicio)} ---{reset}")
                    print(f"{cinza}Caminho completo: {caminho_exercicio}{reset}\n")

                    # Executa o exercício
                    subprocess.run(["python", caminho_exercicio])

                    while True:
                        retorno = input(f"\n{reset}Digite '{amarelo}{negrito}M{reset}' para voltar ao menu ou '{vermelho}{negrito}C{reset}' para cancelar: {reset}")
                        if retorno.lower() == 'm':
                            break
                        elif retorno.lower() == 'c':
                            print(f"\n{vermelho}{cancelar_emoticon} Cancelando a operação...{reset}")
                            return

                    # Barra de progresso dos exercícios executados
                    print(f"\n{amarelo}Progresso:{reset}", end=" ")
                    for i in range(1, len(exercicios) + 1):
                        if i in executados:
                            print(f"{verde}{barra_concluida}{reset}", end=" ")
                        else:
                            print(f"{cinza}{barra_pendente}{reset}", end=" ")
                    print(f"\n{verde} {len(executados)}/{len(exercicios)} concluído(s).{reset}")

                    input(f"\nPressione Enter para continuar...")
                    break
                else:
                    print(f"{reset}{cinza}{alerta_emoticon} Opção inválida! Por favor, tente novamente.{reset}\n")
            except ValueError:
                print(f"{reset}{cinza}{alerta_emoticon} Entrada inválida! Por favor, insira um número.{reset}\n")
            except Exception as e:
                print(f"{reset}{cinza}{alerta_emoticon} Erro ao executar o exercício: {e}{reset}\n")

if __name__ == "__main__":
    exibir_menu()
