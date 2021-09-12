# Exemplo: Copiando dois arquivos 24

def copiaArquivo(velhoArquivo, novoArquivo):
 f1 = open(velhoArquivo, "r")
 f2 = open(novoArquivo, "w")
 for texto in f1:
 f2.write(texto)
 f1.close()
 f2.close()
 
copiaArquivo("velho.txt", "novo.txt")