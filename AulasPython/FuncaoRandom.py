# Exemplo: escrevendo números aleatórios no monitor

import random

def escreverNumerosAleatorios(qtdNumeros):
 for i in range(qtdNumeros):
 print(random.randint(0,100))

escreverNumerosAleatorios(100)
