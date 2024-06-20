'''
Curso : Estructura de datos y algoritmos
Modulo : Rates of growth
Author : Jaime Gomez
Version : 1.0
Date : 28/02/2024
'''

n = 10**2

# ------------- Loops -----------
for i in range(0,n):
    print(f"i = {i}")

# ------------- Nested Loops -----------
for i in range(0,n):
    for j in range(0,n):
        print (f"i={i}; j={j}")

# ------------- Consecutive statements -----------
for i in range(0,n):
    print ("i={}".format(i))

for i in range(0,n):
    for j in range(0,n):
        print ("i={}; j={}".format(i,j))

# ------------- If-then-else statements -----------
if n == 1 :
    print(n)
else:
    for i in range(0,n):
        print(i)

# ------------- Logarithm Complexity -----------
def logarithms(n): 
    i=1
    while i <= n: 
        i= i * 2 
        print(i)

logarithms(100)
    