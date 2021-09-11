# Calculadora Soma ou Multiplicaçao
# anomalia se op <> M e bugs 

op = input("Deseja somar (S) ou multiplicar (M)?")

x = int(input("Digite o primeiro numero:"))

y = int(input("Digite o segundo numero:"))

if (op == "S"):
r = x + y
print("O resultado da soma é", r)
else:
r = x * y
print("O resultado da multiplicação é", r)
