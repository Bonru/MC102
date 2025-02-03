###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Mansão Mal Assombrada II
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

'''
Função para encontrar um caminho até a saída, essa função deve ser implementada
de forma recursiva. A função recebe a matriz representando a mansão, um valor
booleano p, indicando se você já encontrou o escudo e está protegido dos
fantasmas, e valores inteiros a, l e c, representando o andar atual, a linha
atual e a coluna atual, respectivamente. A função deve retornar True, caso
exista uma saída, ou False, caso contrário.'''

def simula_caminho(mansao, p, a, l, c):
    print(a,l,c)
    #declarando direcoes
    norte = mansao[a][l-1][c]
    sul = mansao[a][l+1][c]
    leste = mansao[a][l][c+1]
    oeste = mansao[a][l][c-1]
    if a == 0 and A > 1:
        cima = mansao[a+1][l-1][c]
    if a > 0:
        baixo = mansao[a-1][l][c]

    #verifica se a saida esta adjacente
    if perto_saida(mansao, a, l, c) == True:
        return True

    if perto_escudo(mansao, a, l, c) == True:
        p = True

    #ja passei por aqui!!
    mansao[a][l][c] = "X"
    
    print(mansao)
    
    #qual direcao tomar
    if norte != "*" and norte != "X":#se da pra passar pra norte
        if norte != "F":
            l += 1
        elif norte == "F" and p == True:#se da pra passar norte pra tendo escudo
            l += 1
    elif norte == "X" and sul != "*":#se ja passou por norte
        l -= 1

    if sul != "*" and sul != "X":#se da pra passar pra sul
        if sul != "F":
            l -= 1
    elif sul == "X" and norte != "*":#se ja passou por sul
        l += 1

    if oeste != "*" and oeste != "X":#se da pra passar pra oeste
        if oeste != "F":
            c -= 1
    elif oeste == "X" and leste != "*":#se ja passou por oeste
        c += 1

    if leste != "*" and leste != "X":#se da pra passar pra leste
        if leste != "F":
            c += 1
    elif leste == "X" and oeste != "*":#se ja passou por leste
        c -= 1

    simula_caminho(mansao, p, a, l, c)
    pass

def perto_saida(mansao, a, l, c):
    if mansao[a][l][c] == "=":
        return True
    if mansao[a][l+1][c] == "=":
        return True
    if mansao[a][l-1][c] == "=":
        return True
    if mansao[a][l][c+1] == "=":
        return True
    if mansao[a][l][c-1] == "=":
        return True
    else:
        return False

def perto_escudo(mansao, a, l, c):
    if mansao[a][l][c] == "@":
        return True
    if mansao[a][l+1][c] == "@":
        return True
    if mansao[a][l-1][c] == "@":
        return True
    if mansao[a][l][c+1] == "@":
        return True
    if mansao[a][l][c-1] == "@":
        return True
    else:
        return False

# Leitura da matriz representando a mansão
A, L = [int(v) for v in input().split()]
mansao = [[] for _ in range(A)]

for andar in range(A-1,-1,-1):
    for _ in range(L):
      mansao[andar].append(list(input()))
    if andar > 0:
        input()

a0, l0, c0 = [int(v) for v in input().split()]

# Simulação do caminho
posicoes_passadas = []
escapou = simula_caminho(mansao, False, a0, l0, c0)

# Impressão da saída
if escapou:
    print("Caminho para saida encontrado com sucesso.")
else:
    print("Nao existe caminho seguro para a saida.")