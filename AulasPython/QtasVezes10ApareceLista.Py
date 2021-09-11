# Exemplo: contar quantas vezes o elemento de valor 10 aparece na lista 

lista = [1, 10, 2, 10, 3, 10, 4, 5, 6] 
cont = 0 

for i in range(len(lista)): 
 if lista[i] == 10: 
 cont += 1 

print(cont) 