# Exemplo: lendo números de um arquivo e escrevendo a média

def escreverMedia(qtdNumeros, nomeArquivo):
 arquivoNumeros = open(nomeArquivo)
 soma = 0
 for i in range(qtdNumeros):
 num = float(arquivoNumeros.readline())
 soma += num
 arquivoNumeros.close()
 return soma/qtdNumeros

print(escreverMedia(100, ‘media.txt’))