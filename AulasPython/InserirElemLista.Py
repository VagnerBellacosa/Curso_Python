# Inserir o elemento 10 na posição 2 de uma lista (ou seja, inserir como terceiro elemento da lista) 

lista = [1, 2, 3, 4] 
lista.append(0) 
pos = 2 

#abre espaço para inserir o novo elemento 
for i in range(len(lista)-1, pos-1, -1): 
 lista[i] = lista[i-1] 
lista[pos] = 10 

print(lista) 
