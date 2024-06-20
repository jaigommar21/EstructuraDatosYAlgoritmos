'''
Enunciado de la 1ra practica
@author : Jaime Gómez

'''

'''
15, 20, 10, -50, 40, -450, 1950, -8420, 38610, -173530, 781000, -3519530,  15851830, -71401140

3x5 4x5 2x5 -10x5  8x5  -90x5 -390x5  

   X        X         X           X              X                X                     X

       -70     -400      -7970     
'''

import numpy as np

d =  [15, 20, 10, -50, 40, -450, 1950, -8420, 38610, -173530, 781000, -3519530,  15851830, -71401140]

d = np.array(d)

print(d/5)

import matplotlib.pyplot as plt

# Valores de la serie
valores_serie = [15, 20, 10, -50, 40, -450, 1950, -8420, 38610,
                  -173530, 781000, -3519530, 15851830, -71401140]

indices = list(range(1, len(valores_serie) + 1))

plt.figure(figsize=(10, 5))
plt.plot(indices, valores_serie, marker='o', linestyle='-', color='b')
plt.title('Gráfico de la Serie')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)

# Mostrar el gráfico
plt.show()


exit(-1)


for i in range(1,100,1):
    for j in range(1,100,1):
        print("hola mundo")


# Empty Stack
stack = []
print("-------------------------")
print("Begin  -->",stack)
stack.append(11)      #  Operation type?     
print("-------------------------")
print("???? 11 -->",stack)


