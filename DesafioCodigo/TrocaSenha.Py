casos = int(input())
cont = int(0)
#completes os espaços vazios com sua solução
let = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 's', 'S']

while (  casos > cont  ):

    senha = input()

    var = 1

    for x in range(len(senha)):
        if senha[x] in let:
            var *= 3
        else:
            var *= 2

    cont = cont + 1   
    
    print(var)