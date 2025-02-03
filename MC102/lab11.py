###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Loteamento
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

loteamento = [["x" for _ in range(15)] for _ in range(15)]

# Leitura de dados
r_horizontal = input().split()
for j in r_horizontal:
    for n in range(15):
        loteamento[int(j)][n] = "."
        
r_vertical = input().split()
for j in r_vertical:
    for n in range(15):
        loteamento[n][int(j)] = "."

n_jogadores = int(input())

def varredura(lote):
    falha = False
    #lote = input().split
    xi, xo, yi, yo = int(lote[0]), int(lote[2]), int(lote[1]), int(lote[3])
    for x in range(xi,xo+1):
        for y in range(yi,yo+1):
            if loteamento[x][y] != "x":
                falha = True
    return falha

def construcao(lote, comprador):
    xi, xo, yi, yo = int(lote[0]), int(lote[2]), int(lote[1]), int(lote[3])
    for x in range(xi,xo+1):
        for y in range(yi,yo+1):
            loteamento[x][y] = str(comprador)
   
# Processamento
for j in range(n_jogadores):
    lote = input().split()
    if varredura(lote) == False:
        construcao(lote, j+1)

# Impressão da saída
for linha in loteamento:
  print(" ".join(linha))