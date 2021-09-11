# Exemplo de Vetor

def maior(vetor): 
 #ordena o vetor usando Bubble Sort 
 if len(vetor) > 1:
  for j in range(0,len(vetor)): 
   for i in range(0,len(vetor)-1): 
    if vetor[i]>vetor[i+1]: 
 aux = vetor[i+1] 
 vetor[i+1] = vetor[i] 
 vetor[i] = aux 
 
 #retorna o último elemento do vetor 
 return vetor[len(vetor)-1] 
v = [5, 4, 3, 2, 1] 
print(v) 
m = maior(v) 
print(m) 
print(v)