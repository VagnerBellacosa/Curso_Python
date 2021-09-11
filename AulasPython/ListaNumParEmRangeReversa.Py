# Programa que retorna uma lista com todos os números pares entre 2 e um número n, inclusive, em ordem reversa 

n = eval(input('Digite um numero: ')) 

lista = [] 

for i in range(2,n+1,2): 
lista = [i] + lista 
print(lista)

