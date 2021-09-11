# Programa que cria uma matriz n x m preenchida com 

zeros e a imprime no formato de matriz
n = int(input('Digite a dimensão n da matriz: '))
m = int(input('Digite a dimensão m da matriz: '))
matriz = []

for i in range(n):
matriz.append([0]*m)

#imprimir em formato de matriz
for i in range(n):
print(matriz[i])
