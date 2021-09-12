# Exemplo: escrevendo números aleatórios em um arquivo

import random

def escreverNumerosAleatorios(qtdNumeros, nomeArquivo):
 arquivoNumeros = open(nomeArquivo, ‘w’)
 for i in range(qtdNumeros):
 arquivoNumeros.write(str(random.randint(0,100))
 arquivoNumeros.write("\n")
 
 arquivoNumeros.close()
escreverNumerosAleatorios(100, ‘aleatorios.txt’)