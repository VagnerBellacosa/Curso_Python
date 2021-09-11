

# Encontrar um elemento dentro da lista 
# Encontrar o elemento de valor 10 na lista [1, 2, 10, 5, 20] e retornar a posição em que ele foi encontrado 

lista = [1, 2, 10, 5, 20] 
valor = 10 
pos = -1 

for i in range(len(lista)-1,-1,-1): 
 if lista[i] == valor: 
 pos = i 
print(pos)