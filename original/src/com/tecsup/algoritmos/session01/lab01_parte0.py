'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
Version : 1.0
Date : 28/02/2024
'''

import matplotlib.pyplot as plt

##  100 --> 0.01
##  1000 --> 0.02
##  100000 --> 0.05


data = {100:0.01, 1000:0.02, 10000:0.05}
        
plt.scatter(x=data.keys(), y=data.values(), color="Red")
plt.title('Loops')
plt.xlabel('Iteractions')
plt.ylabel('Time(s)')
plt.show()


