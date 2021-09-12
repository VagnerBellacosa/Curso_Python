# Funcao maior 

def maior(vetor): 
 vetor.sort() 
 return vetor[len(vetor)-1] 

v = [5, 4, 3, 2, 1] 

print(v) 

m = maior(v) 

print(m) 

print(v)