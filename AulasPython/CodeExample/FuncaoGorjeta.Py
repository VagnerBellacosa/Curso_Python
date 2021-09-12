# Funcao Gorjeta

def calcular_gorjeta(valor, percentual=10): 
 return valor * percentual/100 

gorjeta = calcular_gorjeta(400) 

print('O valor da gorjeta de 10% de uma conta de R$ 400 eh', gorjeta) 

gorjeta = calcular_gorjeta(400, 5) 

print('O valor da gorjeta de 5% de uma conta de R$ 400 eh', gorjeta)