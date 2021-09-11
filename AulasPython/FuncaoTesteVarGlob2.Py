# Funcao exemplo variaveis globais 2

def maior(): 
 global m
 if a > b: 
 m = a 
 else: 
 m = b

m = 0 
a = 1 
b = 2 

maior() 

print(m) 