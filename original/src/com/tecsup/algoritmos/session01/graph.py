
'''
Curso : Estructura de datos y algoritmos
Modulo : Grafico
Author : Jaime Gomez
'''

import matplotlib.pyplot as plt

def draw(x,y, color = "g", title='', label_x='', label_y=''):
        
    plt.scatter(x, y, color=color)
    plt.title(title)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    #plt.savefig("img/factorial-01")
    plt.show()

