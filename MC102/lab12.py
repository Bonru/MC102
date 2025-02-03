###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Mansão Mal Assombrada I
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

# Leitura da matriz representando a mansão
A, L = [int(v) for v in input().split()]
mansao = [[] for _ in range(A)]

for andar in range(A-1,-1,-1):
    for _ in range(L):
      mansao[andar].append(list(input()))
    if andar > 0:
      input()

# Leitura das posições de cada fantasma e de cada caçador
posicoes_fantasmas = []
posicoes_cacadores = []

n_fantasmas = int(input())
for i in range(n_fantasmas):
   posicoes_fantasmas.append(input())

n_cacadores = int(input())
for n in range(n_cacadores):
   posicoes_cacadores.append(input())


# Simulação do movimento dos fantasmas
fantasmas_capturados = 0
cacadores_capturados = 0

for pi in posicoes_fantasmas:
   movimentos = 0
   pi = pi.split()
   a, l, c = int(pi[0]), int(pi[1]), int(pi[2])
   while movimentos <= 100:
    # VER SE CAPTURA CACADOR
    for p in range(len(posicoes_cacadores)):
       posicao = posicoes_cacadores[p]
       if posicao.split() == [str(a),str(l),str(c)]:
          posicoes_cacadores.pop(p)
          cacadores_capturados += 1
          break
       
    # VERIFICAR SE NÃO ULTRAPASSOU LIMITES
    if not(a in range(0,A) and l in range(0,L+1) and c in range(0,len(mansao[0][0]))):
        break
    if mansao[a][l][c] == "N":
        l -= 1
    elif mansao[a][l][c] == "S":
        l += 1
    elif mansao[a][l][c] == "O":
        c -= 1
    elif mansao[a][l][c] == "L":
        c += 1
    elif mansao[a][l][c] == "C":
        a += 1
    elif mansao[a][l][c] == "B":
        a -= 1
    elif mansao[a][l][c] == "X":
        fantasmas_capturados += 1
        break
    else:
       break
    movimentos += 1


# Impressão da saída
print("fantasmas capturados:", fantasmas_capturados)
print("caçadores capturados:", cacadores_capturados)