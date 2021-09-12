
# Ordenar uma lista 
# Selection Sort

lista = [10, 9, 8, 7, 5, 3, 4, 3, 1, 2, 11] 
lista_ordenada = [] 
tam = len(lista) 

for i in range(tam): 
 menor = lista[0] 
 for j in range(len(lista)): 
 if lista[j] < menor: 
 menor = lista[j] 
 pos_menor = j
 lista_ordenada.append(menor) 
 lista.remove(menor) 

print(lista_ordenada) 