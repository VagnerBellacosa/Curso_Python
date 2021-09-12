# Exemplo: lendo números de um arquivo e escrevendo a média

def escreverMedia(nomeArquivo):
 arquivoNumeros = open(nomeArquivo)
 soma = 0
 qtdNumeros = 0
 for num in arquivoNumeros:
 num = float(num)
 soma += num
 qtdNumeros += 1
 arquivoNumeros.close()
 return soma/qtdNumeros

print(escreverMedia(‘media.txt’))
