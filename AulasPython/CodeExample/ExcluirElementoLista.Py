# Excluir um elemento 
# Excluir a primeira ocorrência do elemento de valor 4 da lista [1, 4, 5, 6, 4, 7] 
lista = [1, 4, 5, 6, 4, 7] 
valor = 4 
removeu = False 
temp = [] 

for i in range(len(lista)): 
 if lista[i] != valor or removeu: 
 temp.append(lista[i]) 
 else: 
 removeu = True
lista = temp

print(lista)