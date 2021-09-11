# Calculadora Soma ou Multiplicaçao
# anomalia se op <> M solucionada
# bug de numero x ou y invalido
# Versao melhorada

op = input("Deseja somar (S) ou multiplicar (M)?")

if (op == "S" or op =="M"):
x = int(input("Digite o primeiro numero:"))
y = int(input("Digite o segundo numero:"))

if (op == "S"):
r = x + y
print("O resultado da soma é", r)
elif (op == "M"):
r = x * y
print("O resultado da multiplicação é", r)
else:
print("Opção inválida")
