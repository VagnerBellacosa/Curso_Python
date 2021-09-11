# Soma de Números Aleatórios com while

from random import randint

x = int(input('Digite um numero: '))
soma = 0
contador = 0

while contador < x:
numero_sorteado = randint(1,10)
print(numero_sorteado)
soma = soma + numero_sorteado
contador = contador + 1
print('A soma eh', soma)