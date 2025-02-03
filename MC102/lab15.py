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
def simula_caminho(mansao, p, a, l, c,contador,posicoes_visitadas,procura_escudo):
    posicao_atual = mansao[a][l][c]

    direcoes = ["norte", "sul", "leste", "oeste"]
    aux = [a,l,c]
    norte = mansao[a][l-1][c]
    sul = mansao[a][l+1][c]
    leste = mansao[a][l][c+1]
    oeste = mansao[a][l][c-1]
    if len(mansao) > 1 and a <= (len(mansao)-2):
        cima = mansao[a+1][l][c]
        direcoes.append("cima")
    if a > 0:
        baixo = mansao[a-1][l][c]
        direcoes.append("baixo")

    if procura_escudo == True:
        p = verifica_escudo(norte,sul,leste,oeste)

    verifica_saida(norte,sul,leste,oeste)  
        
    for direcao in direcoes:
        if (direcao == "norte" and norte != "*" and norte != "F" and [a,l-1,c] not in posicoes_visitadas) or (direcao == "norte" and norte == "F" and p == True and [a,l-1,c] not in posicoes_visitadas):
            l -= 1
            mudou_posicao(mansao,p,aux,a,l,c,contador,posicoes_visitadas,procura_escudo)
        if (direcao == "sul" and sul != "*" and sul != "F" and [a,l+1,c] not in posicoes_visitadas) or (direcao == "sul" and sul == "F" and p == True and [a,+1,c] not in posicoes_visitadas):
            l += 1
            mudou_posicao(mansao,p,aux,a,l,c,contador,posicoes_visitadas,procura_escudo)
        if (direcao == "leste" and leste != "*" and leste != "F" and [a,l,c+1] not in posicoes_visitadas) or (direcao == "leste" and leste == "F" and p == True and [a,l,c+1] not in posicoes_visitadas):
            c += 1
            mudou_posicao(mansao,p,aux,a,l,c,contador,posicoes_visitadas,procura_escudo)
        if (direcao == "oeste" and oeste != "*" and oeste != "F" and [a,l,c-1] not in posicoes_visitadas) or (direcao == "oeste" and oeste == "F" and p == True and [a,l,c-1] not in posicoes_visitadas):
            c -= 1
            mudou_posicao(mansao,p,aux,a,l,c,contador,posicoes_visitadas,procura_escudo)
        if direcao == "cima" and cima == "#" and [a+1,l,c] not in posicoes_visitadas and posicao_atual == "#":
            a += 1
            mudou_posicao(mansao,p,aux,a,l,c,contador,posicoes_visitadas,procura_escudo)
        if direcao == "baixo" and baixo == "#" and [a-1,l,c] not in posicoes_visitadas and posicao_atual == "#":
            a -= 1
            mudou_posicao(mansao,p,aux,a,l,c,contador,posicoes_visitadas,procura_escudo)
        
        mudou_posicao(mansao,p,aux,a,l,c,contador,posicoes_visitadas,procura_escudo)
        
def mudou_posicao(mansao,p,aux,a,l,c,contador,posicoes_visitadas,procura_escudo):
    posicoes_visitadas.append([a,l,c])
    contador += 1
    if contador >= 300:
        contador = 0
        return 0
    if aux != [a,l,c]:
        if p == True and procura_escudo == True:
            contador = 0
            posicoes_visitadas = []
            mansao = aniquila_fantasmas(mansao)
            procura_escudo = False
        simula_caminho(mansao,p,a,l,c,contador,posicoes_visitadas,procura_escudo)

def verifica_escudo(norte,sul,leste,oeste):
    if norte == "@" or sul == "@" or leste == "@" or oeste == "@":
        return True
    else:
        return False
    
def verifica_saida(norte,sul,leste,oeste):
    if norte == "=" or sul == "=" or leste == "=" or oeste == "=":
        print("Caminho para saida encontrado com sucesso.")
        quit()
    else:
        return False

def aniquila_fantasmas(mansao):
    for i in mansao:
        for j in i:
            if j == "F":
                j = "."
    return mansao

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
contador = 0
posicoes_visitadas = []
procura_escudo = True
escapou = simula_caminho(mansao, False, a0, l0, c0, contador,posicoes_visitadas,procura_escudo)


# Impressão da saída
print("Nao existe caminho seguro para a saida.")