# Recebe 3 alunos e apura a media, motivando os melhores

nome1 = input('Informe o nome do aluno 1: ') 
nome2 = input('Informe o nome do aluno 2: ') 
nome3 = input('Informe o nome do aluno 3: ') 

nota1 = eval(input('Informe a nota de ' + nome1 + ':')) 
nota2 = eval(input('Informe a nota de ' + nome2 + ':')) 
nota3 = eval(input('Informe a nota de ' + nome3 + ':')) 

media = (nota1 + nota2 + nota3)/3 

print('A media da turma foi', media) 

if nota1 > media: 
 print('Parabens', nome1) 

if nota2 > media: 
 print('Parabens', nome2) 

if nota3 > media: 
 print('Parabens', nome3)