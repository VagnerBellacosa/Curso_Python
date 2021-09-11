
# Inserir os elementos de lista2 ao final de lista1 

lista1 = [1, 2, 3, 4] 
lista2 = [5, 6, 7] 

for i in range(len(lista2)): 
 lista1.append(lista2[i])

print(lista1)