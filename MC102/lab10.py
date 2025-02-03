#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caçadores de Tesouros
# Nome:
# RA:
#####################################################

# Leitura do mapa
n, m = [int(i) for i in input().split()]

mapa = []
for _ in range(n):
  linha = [int(i) for i in input().split()]
  mapa.append(linha)

n_jogadores = int(input())
lista_tesouro = []

# Leitura e processamento dos movimentos dos personagens
for i in range(n_jogadores):
    x, y = [int(i) for i in input().split()]
    tesouro = mapa[x][y]#####
    mapa[x][y] = 0      #se jogador nasce com tesouro
    movimento = str(input())
    lista_movimento = [*movimento]
    for h in lista_movimento:
        if h == "N":
            x-=1
        elif h == "S":
            x+=1
        elif h == "L":
            y+=1
        elif h == "O":
            y-=1
        #pegar tesouros
        if mapa[x][y] != 0:
            if tesouro == 0:
                tesouro = mapa[x][y]
                mapa[x][y] = 0
            elif tesouro != 0 and tesouro < mapa[x][y]:
                var1 = mapa[x][y]
                mapa[x][y] = tesouro
                tesouro = var1
    lista_tesouro.append(tesouro)

# Impressão da saída
for k in range(n_jogadores):
    print("Caçador " + str(k+1) + ':', lista_tesouro[k])