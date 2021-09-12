# inicializa vetor de notas com 0 

notas = [0] * 3 

soma = 0 

# preenche vetor de notas, sem usar append 

for i in range(3): 
 notas[i] = eval(input("Digite a nota 

do aluno " + str(i) + ": ")) 
 soma = soma + notas[i] 

print("A media da turma é", soma/3)
