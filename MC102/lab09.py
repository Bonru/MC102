###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Criptografia Cíclica
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

# Leitura da entrada
codigo, mensagem, resposta = input().upper(), input().upper(), ''

# Decodificação da mensagem
codigo_lista = [*codigo]
lista = mensagem.split()
for palavra in lista:
    letras_palavra = [*palavra]
    for j in range(len(letras_palavra)):
        for t in range(len(codigo_lista)):
            if letras_palavra[j] == codigo_lista[t]:
                if t-1 >= 0:
                    letras_palavra[j] = codigo_lista[t-1]
                else: 
                    letras_palavra[j] = codigo_lista[len(codigo_lista)-1]
                break
    for x in range(len(letras_palavra)):
        resposta += "" + letras_palavra[x].lower()
        if x == len(letras_palavra)-1:
            resposta += " "

# Impressão da saída

resposta = resposta.capitalize()
resposta = resposta.rstrip()
print(resposta)
