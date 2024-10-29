import random

personagens = ['um cavaleiro', 'uma astronauta', 'um dragão', 'um robô', 'um detetive', 'uma princesa']
acoes = ['encontrou um tesouro', 'lutou contra monstros', 'descobriu um segredo', 'viajou no tempo', 'salvou o mundo', 'resolveu um mistério']
locais = ['em uma floresta encantada', 'no espaço sideral', 'no fundo do mar', 'em uma cidade futurista', 'em um castelo abandonado', 'em uma ilha deserta']

def criar_historia():
    personagem = random.choice(personagens)
    acao = random.choice(acoes)
    local = random.choice(locais)
    
    historia = f"Era uma vez {personagem} que {acao} {local}."
    return historia

historia_gerada = criar_historia()
print(historia_gerada)
