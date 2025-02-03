###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Investimento em Renda Fixa
# Nome:
# RA:
###################################################

# leitura de dados

montante = int(input())
d = int(input())
taxapoupanca = int(input())
taxatesouro = int(input())

# cálculo dos rendimentos
if d <= 180:
	tributo = 0.225
elif 181 <= d <= 360:
	tributo = 0.2
elif 361 <= d <= 720:
	tributo = 0.175
elif 720 <= d:
	tributo = 0.15
	
poupanca = montante/100 * taxapoupanca
tesouro = (montante/100 * taxatesouro) * (1-tributo)

# Impressão da saída
print("Rendimento poupança: {:.2f}".format(poupanca))
print("Rendimento tesouro: {:.2f}".format(tesouro))

if poupanca > tesouro:
	print("Maior rendimento: poupança")
else:
	print("Maior rendimento: tesouro")