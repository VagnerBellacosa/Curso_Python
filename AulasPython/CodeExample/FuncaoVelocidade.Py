# Funcao velocidade

def calcula_tempo(velocidade, distancia): 
 tempo = distancia/velocidade 
 return tempo 

def calcula_distancia(velocidade, tempo): 
 distancia = velocidade * tempo 
 return distancia 

t = calcula_tempo(10, 5) 

print(t) 

d = calcula_distancia(5, 4) 

print(d)