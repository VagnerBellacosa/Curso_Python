# Exemplo: lendo números do teclado e escrevendo a média

def escreverMedia(qtdNumeros):
 soma = 0
 for i in range(qtdNumeros):
 num = int(input("Digite o número:"))
 soma += num
 return soma/qtdNumeros

print(escreverMedia(100))
