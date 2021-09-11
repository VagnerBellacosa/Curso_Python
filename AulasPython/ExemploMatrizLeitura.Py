# Preencher a matriz por leitura

turma = []
for i in range(3):

# cria linha vazia
linha = []
for j in range(5):

#vai adicionando as notas na linha
linha.append(int(input('Digite a nota 
[' + str(i) + ',' + str(j) + ']:')))

#adiciona a linha na matriz turma
turma.append(linha