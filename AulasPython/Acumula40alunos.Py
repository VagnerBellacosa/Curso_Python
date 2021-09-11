num_alunos = 40 

nomes = [] 
notas = [] 
media = 0 

for i in range(num_alunos): 
 nomes.append(input('Informe o nome do aluno: ')) 
 notas.append(eval(input('Informe a nota de ' + nomes[i] + ': '))) 
 media = media + notas[i] 

media = media / num_alunos

print('A media da turma eh ', media) 

for i in range(num_alunos): 
 if notas[i] > media: 
 print('Parabens', nomes[i]) 
