# Calculo da distancia em dois pontos em um coordenada cartesiana

import math

x1 = int(input("Entre com a coordenada x do 1o. ponto:"))
y1 = int(input("Entre com a coordenada y do 1o. ponto:"))
x2 = int(input("Entre com a coordenada x do 2o. ponto:"))
y2 = int(input("Entre com a coordenada y do 2o. ponto:"))

cateto1 = math.fabs(y2-y1)
cateto2 = math.fabs(x2-x1)

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print("A distancia entre os dois pontos é", hipotenusa)
