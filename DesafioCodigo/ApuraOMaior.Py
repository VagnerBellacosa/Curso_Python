import math
a, b ,c= map(eval, input().split())

maior1 = (  a + b + abs(a-b)  )/2
maior2 = ( maior1 + c + abs(maior1 - c) )/2

print("%i eh o maior" %maior2)
