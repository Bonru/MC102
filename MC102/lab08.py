###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Anagramas
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

# Leitura das palavras
N, dicionario, a1 = int(input()), [], []
for i in range(N):
    palavra = input()
    dicionario.append(palavra)

# Agrupamento dos anagramas


# Impressão da saída

for j in range(len(dicionario)):
    lista_final = []
    if j not in a1:
        for k in range(len(dicionario)):
            if sorted(dicionario[j]) == sorted(dicionario[k]):
                lista_final.append(dicionario[k])
                a1.append(k)
    if lista_final != []:
        for q in lista_final:
            if q != lista_final[len(lista_final)-1]:
                print(q,end = "-")
            else:
                print(q)