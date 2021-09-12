# Programa que lê uma lista do teclado, soma 1 aos elementos da lista e imprime a lista resultante 

continua = 's' 

lista = [] 

while (continua == 's' or continua == 'S'): n = eval(input('Digite um numero: ')) lista.append(n) 
 continua = input('Deseja continuar? (s/n): ') 

print(lista) 

for i in range(len(lista)): 
 lista[i] = lista[i] + 1 
print(lista) 
