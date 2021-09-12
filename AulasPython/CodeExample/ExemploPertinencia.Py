# Teste de Pertinência 
# Retornar True caso o valor 10 pertença à lista, e False caso contrário 

lista = [1, 2, 3, 4] 
valor = 7 
resultado = False 

for i in range(len(lista)): 
 if lista[i] == valor: 
 resultado = True

print(resultado) 