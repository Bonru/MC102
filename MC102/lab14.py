###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Pulo do Gato
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

'''
Função recursiva para simular o caminho do gato. A função recebe
uma matriz representando o mapa do circuito, a posição (linha,coluna)
do gato e a posição (linha, coluna) do petisco. A função deve retornar 
se o gato consegue capturar o petisco.
'''

def pulo_do_gato(mapa, linha_gato, coluna_gato, linha_petisco, coluna_petisco):

    if linha_gato not in range(0,n) or coluna_gato not in range(0,len(mapa[0])):
        print("Petisco não capturado")
        exit()

    posicao = [linha_gato,coluna_gato]

    #print(posicao, mapa[linha_gato][coluna_gato])

    if mapa[linha_gato][coluna_gato] == "V":
        
        valor = distancia("V", linha_gato, coluna_gato, linha_petisco, coluna_petisco)

        if posicao not in posicoes_visitadas:
            if (linha_gato + valor) in range(0,n):
                linha_gato = linha_gato + valor
            else:
                linha_gato - valor

        if posicao in posicoes_visitadas:
            if (linha_gato - valor) in range(0,n):
                linha_gato = linha_gato - valor
            else:
                linha_gato = linha_gato + valor
        return linha_gato, coluna_gato
    
    elif mapa[linha_gato][coluna_gato] == "H":
        valor = distancia("H", linha_gato, coluna_gato, linha_petisco, coluna_petisco)
        if posicao not in posicoes_visitadas:
            coluna_gato = coluna_gato + valor
        if posicao in posicoes_visitadas:
            coluna_gato = coluna_gato - valor
        return linha_gato, coluna_gato
    
    elif mapa[linha_gato][coluna_gato] == "*":
        print("Petisco capturado")
        exit()


def distancia(direcao, linha_gato, coluna_gato, linha_petisco, coluna_petisco):

    if direcao == "H":
        if abs(coluna_petisco - coluna_gato) > abs(coluna_petisco - (coluna_gato + 1)):
            if (coluna_gato + 1) in range(len(mapa[0])):
                return 1
            else:
                return (-1)
        elif coluna_petisco - coluna_gato > coluna_petisco - coluna_gato - 1 and coluna_gato != 0:
            if (coluna_gato - 1) in range(len(mapa[0])):
                return (-1)
            else:
                return 1
        elif coluna_gato == 0:
            return (1)
        
    elif direcao == "V":
        if abs(linha_petisco - linha_gato) > linha_petisco - (linha_gato + 1):
            if (linha_gato + 1) in range(0,n):
                return 1
            else:
                return (-1)
        elif linha_petisco - linha_gato > linha_petisco - (linha_gato - 1) and linha_gato != 0:
            if (linha_gato - 1) in range(0,n):
                return (-1)
            else:
                return 1
        elif linha_gato == 0:
            return (1)

# Leitura de dados
n = int(input())
posicoes_visitadas = []
mapa = []
for _ in range(n):
  mapa.append(list(input()))

posicao_gato = input().split()
linha_gato = int(posicao_gato[0])
coluna_gato = int(posicao_gato[1])

for linha in range(len(mapa)):
    for coluna in range(len(mapa[linha])):
       if mapa[linha][coluna] == "*":
            linha_petisco, coluna_petisco = linha, coluna
        
for i in range (1000):
    posicao_antiga = [linha_gato, coluna_gato]
    linha_gato, coluna_gato = pulo_do_gato(mapa, linha_gato, coluna_gato, linha_petisco, coluna_petisco)
    posicoes_visitadas.append(posicao_antiga)

print("Petisco não capturado")

# Verificação se o gato consegue capturar o petisco


# Impressão da resposta