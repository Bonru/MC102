###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Amigos do 495
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

# Leitura da sequência
numeros = [int(i) for i in input().split()]
lista_resultados = []

# Ordenação dos amigos do 495
def repeticao(numero, contador):
    termos = [*str(numero)]
    termos.sort()
    crescente = termos
    crescente = ''.join(crescente)
    decrescente = [*crescente]
    decrescente.reverse()
    decrescente = ''.join(decrescente)
    sub = int(decrescente) - int(crescente)
    if sub != 495 and sub != 0:
        contador += 1
        retorno, numero = repeticao(sub, contador)
        return retorno, numero
    elif sub == 0:
        return("nao deu")
    if sub == 495:
        retorno = contador
        return int(retorno), numero

# Impressão da resposta
lista_resultados = []
for i in numeros:
    contador = 1
    contador, numero_inicial  = repeticao(str(i), contador)
    conjunto = [contador,i]
    lista_resultados.append(conjunto)
final = []
parcial = []

for j in range(1000):
    for l in lista_resultados:
        if j == l[1]:
            parcial.append(l)

for j in range(500):
    for l in parcial:
        if j is l[0]:
            final.append(l)

_ = []
for amigo in final:
    _.append(str(amigo[1]))

resposta = " ".join(_)
print(resposta)

