'''
Curso : Estructura de datos y algoritmos
Modulo : Precision
Author : Jaime Gomez
Version : 1.0
Date : 20/03/2023
'''

# Precision
inc = 0.1
sum = 0
for i in range(10):
    print(i)
    sum += inc
print(sum)

# Solution
from decimal import Decimal

inc = Decimal(str(inc))
sum = Decimal(0)

for i in range(10):
    print(i)
    sum += inc
print(sum)


#print(.1 + .1 + .1 == .3)
