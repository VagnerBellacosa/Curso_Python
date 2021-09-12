# Apura numeros pares entre um range

num1 = int(input('Entre com o valor inicial: '))
num2 = int(input('Entre com o valor final: '))

soma = 0

while num1 <= num2:
if num1 % 2 == 0:
soma = soma + num1
num1 = num1 + 1
print('A soma eh', soma)