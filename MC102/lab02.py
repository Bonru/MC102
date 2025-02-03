###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Um Lanche Antes da Aula
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

# Leitura da entrada
T = int(input())
L1 = int(input())
L2 = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())

#Caso 1
dinheiros1 = L1+12
tempo1 = P1+P2+T

#Caso 2
dinheiros2 = L2+6
tempo2 = P3+T

# Comparação entre as opções e impressão da saída

viavel1 = (tempo1 <= 45)
viavel2 = (tempo2 <= 45)

if viavel1 and viavel2 == True:
    if dinheiros1 > dinheiros2:
        resultado = False
    elif dinheiros1 <= dinheiros2:
        resultado = True
    
elif viavel1 == True and viavel2 == False:
    resultado = True

elif viavel2 == True and viavel1 == False:
    resultado = False

elif viavel1 == False and viavel2 == False:
    if tempo1 > tempo2:
        resultado = False
    elif tempo1 <= tempo2:
        resultado = True

print(resultado)
