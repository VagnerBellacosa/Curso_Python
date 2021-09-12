
# Excluir o elemento da posição 2 da lista [1, 2, 3, 4] 
lista = [1, 2, 3, 4] 
pos = 2 
temp = [] 

for i in range(len(lista)): 
 if i != pos: 
 temp.append(lista[i]) 
lista = temp
print(lista) 
