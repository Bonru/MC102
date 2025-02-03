###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Nota de MC102
# Nome: Bruno Falqueto Busato
# RA: 248344
###################################################

# Leitura de dados
n_exercicios = int(input())
notas = []
pesos = []

contador = 1 #lista de notas
while contador <= n_exercicios:
    nota = float(input())
    notas.append(nota)
    contador += 1

contador = 1 #lista de pesos
while contador <= n_exercicios:
    peso = float(input())
    pesos.append(peso)
    contador += 1

#calcular média
def calculos(notas,pesos):
    notas_pesadas = []
    for i in range(len(notas)):
        nota_pesada = notas[i] * pesos[i]
        notas_pesadas.append(nota_pesada)

    somatorio = 0
    soma_pesos = 0
    for i in range(len(notas_pesadas)):
        somatorio = somatorio + float(notas_pesadas[i])
        soma_pesos = soma_pesos + float(pesos[i])
    media = somatorio/soma_pesos
    return media
media = calculos(notas,pesos)

# Cálculo da média ponderada dos laboratórios
print("Media laboratorios:", format(media, ".1f").replace(".", ","))

# Verificação da situação do aluno
def verif(media):
    if media >= 5.0:
        situacao = 2
    elif media < 5.0 and media >= 2.5: 
        situacao = 1
    else:
        situacao = 0
    return situacao
situacao = verif(media)

# Caso o aluno tenha sido aprovado por nota
def exame():
    if situacao == 2:
        nota_final = media
        print("Situacao: Aprovado por nota")

    # Caso o aluno tenha sido reprovado por nota
    elif situacao == 0:
        nota_final = media
        print("Situacao: Reprovado por nota")

    # Cálculo da nota do exame, caso o aluno tenha ido para o exame
    elif situacao == 1:
        n_subs = int(input())
        cont, cont2 = 0, 0
        notas, pesos2 = [], []

        #resgatar pesos
        while cont < n_subs:
            index = int(input())
            pesos2.append(pesos[index-1])
            cont += 1

        #atualizar notas do exame
        while cont2 < n_subs:
            notas.append(float(input()))
            cont2 += 1
        
        nota_final = (calculos(notas,pesos2) + media) / 2

        if nota_final >= 5:
            nota_final = 5
        
        return nota_final

nota_final = exame()

# Caso o aluno tenha sido aprovado no exame
if nota_final >= 5.0:
    print("Situacao: Aprovado no exame")

# Caso o aluno tenha sido repravado no exame
elif nota_final < 5.0:
    print("Situacao: Reprovado no exame")

# Saída de dados
print("Nota final:", format(nota_final, ".1f").replace(".", ","))