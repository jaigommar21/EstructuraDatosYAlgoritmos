'''
Curso : Estructura de datos y algoritmos
Modulo : Algoritmos
Author : Jaime Gomez
Version : 1.0
Date : 28/02/2024
'''

# Example : The sum of the first n integers

n = 10**8

# First solution
sum = 0
for i in range(n+1) :
    sum +=i
print(sum)

# Second solution
sum = n * (( n+1 ) / 2)
print(sum)



