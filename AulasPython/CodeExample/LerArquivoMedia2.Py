#Agora usando while...

def escreverMedia(nomeArquivo):
 arquivoNumeros = open(nomeArquivo)
 soma = 0
 qtdNumeros = 0
 num = arquivoNumeros.readline()
 while num != "":
 num = float(num)
 soma += num
 qtdNumeros += 1
 num = arquivoNumeros.readline()
 arquivoNumeros.close()
 return soma/qtdNumeros

print(escreverMedia(‘media.txt’))