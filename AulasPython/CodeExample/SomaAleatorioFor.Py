#Soma de Números Aleatórios com for

from random import randint

x = int(input('Digite um numero: '))
soma = 0

for contador in range(x):
numero_sorteado = randint(1,10)
print(numero_sorteado)
soma = soma + numero_sorteado
print('A soma eh', soma)