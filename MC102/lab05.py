###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - A Última Rodada
# Nome:
# RA:
###################################################

# Leitura da primeira linha
N, V, P = input().split()
N = int(N)
V = int(V)
P = int(P)

# Leitura da roleta

i = 0
lista = [] #lista de possivbilidades da roleta
while i < N:
    ação = input()
    lista.append(ação)
    i += 1

dinheiros = [] #lista dos possiveis valores apos giro da roleta

for j in range(len(lista)):
    termo = lista[j].split() #ação da lista sendo trabalhada

    if "%" in termo: #se for percentual
        percentual = float(termo[1]) * P / 100
        if "+" in termo:
            dinheiros.append(P + percentual)
        elif "-" in termo:
            dinheiros.append(P - percentual)
            
    elif "%" not in termo: #se nao for percentual
        valor = float(termo[1])
        if "+" in termo:
            dinheiros.append(P + valor)
        elif "-" in termo:
            dinheiros.append(P - valor)
            if (P - valor) <= 0:
                dinheiros.pop()
                dinheiros.append(0)
    

# Calculo da probabilidade
favoraveis = 0 #chances favoraveis
soma = 0 #premio total a ser dividido pelo número de secoes da roleta

for w in dinheiros:
    if w >= V:
        favoraveis += 1
    soma += float(w)

prob_viagem = favoraveis / N * 100
premio_medio = soma / N

# Imprime a probabilidade do premio final ser suficiente para a viagem
print("{:.2f}%".format(prob_viagem))
# Imprime o valor médio do premio final a ser recebido
print("R$ {:.2f}".format(premio_medio))