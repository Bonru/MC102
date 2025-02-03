###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Gráfico de Recorrência
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################
# Leitura de dados
import math
N, lista = int(input()), []
for i in range(N):
    lista.append(float(input()))
limiar, contador1, contador2, lista2 = float(input()), 1, 1,[]
# Impressão do gráfico de recorrência
for i in lista:
    lista2 = []
    while contador1 <= N:
        conta = math.sqrt((i - lista[contador1-1])**2)
        if conta <= limiar:
            lista2.append(0)
        else:
            lista2.append(1)
        if contador2 % N == 0:
            print(lista2[contador1-1])
        elif contador2 % N != 0:
            print(lista2[contador1-1], end=' ')
        contador1, contador2 = contador1 + 1, contador2 + 1
    contador1, contador2 = 1, 1