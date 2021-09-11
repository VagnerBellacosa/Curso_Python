# Variação do Exemplo Contar Pares

matriz = []

for i in range(3):
linha = []

for j in range(3):

linha.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
matriz.append(linha)

#contar pares
pares = 0

for linha in matriz:

for valor in linha:

if valor % 2 == 0:
pares = pares + 1

#imprimir em formato de matriz
for i in range(3):
print(matriz[i])

#imprimir qtde de números pares
print('A matriz contém', pares, 'números pares’)