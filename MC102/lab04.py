###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Batalha Pokémon
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

# Leitura do hp e velocidade dos pokémons
vidas = [int(input()),int(input())] #ivy =0 e pika=1

vi = int(input())
vp = int(input())

poke = ['Ivysaur', 'Pikachu']

ordem =70000
if vi >= vp:
    ordem = 1
elif vp > vi:
    ordem = 0

contador = 1


# Leitura dos ataques dos turnos
p = 1
while p > 0:
    forca = int(input())
    multiplicador = float(input())

    if vidas[0]>0 and vidas[1] > 0:
        vidas[ordem] -= forca * multiplicador
    
    if ordem == 1:
        ordem = 0
    else:
        ordem = 1
    
    if contador == 2:
        if vidas[0] > 0 and vidas[1] > 0:
            print('HP Ivysaur =',int(vidas[0]))
            print('HP Pikachu =',int(vidas[1]))
        else:
            break
        contador = 1

    elif contador == 1:
        contador = 2



# Impressão do vencedor

if vidas[0] > vidas[1]:
    vidas[1] = 0
    print('HP Ivysaur =',int(vidas[0]))
    print('HP Pikachu =',int(vidas[1]))
    print('Pokémon Vencedor: Ivysaur')
    print('HP do Vencedor:', int(vidas[0]))
elif vidas[1] > vidas[0]:
    vidas[0] = 0
    print('HP Ivysaur =',int(vidas[0]))
    print('HP Pikachu =',int(vidas[1]))
    print('Pokémon Vencedor: Pikachu')
    print('HP do Vencedor:', int(vidas[1]))