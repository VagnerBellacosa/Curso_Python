# Imprime numeros pares entre 100 e 200

num = 100

contador_pares = 0

while num <= 200:
if num % 2 == 0:
contador_pares = contador_pares + 1
num = num + 1

print(contador_pares)