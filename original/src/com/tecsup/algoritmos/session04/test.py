'''
def calcularMCD(a,b, MCD):
    i=min(a,b)
    while MCD==False and i>1:
        if a % i == 0 and b % i == 0:
            print("El MCD es ", i)
            MCD=True
        else:
            i = i-1
            if i == 1:
                print("Estos dos nUmeros no tienen MCD")
    

Numeros_ingresados_son_correctos=False
while Numeros_ingresados_son_correctos==False:12
    a=int(input("Ingrese el primer nUmero :  "))
    b=int(input("Ingrese el segundo nUmero :  "))
    MCD=False
    if a>0 and b>0 and a!=b:
        Numeros_ingresados_son_correctos = True
        calcularMCD(a,b, MCD)
    else: 
        if a==b:
            print("Los nUmeros son iguales. Intentalo otra vez")
        else:
            print("Los nUmeros no son correctos. Intentalo otra vez")


'''

'''           
import matplotlib.pyplot as plt
notas_alumnos = [16, 18, 14, 18, 20, 16, 18, 20, 16, 8]
cod_alumnos   = [1, 2, 3, 4, 5, 6, 7,  8, 9, 10]
plt.scatter(cod_alumnos, notas_alumnos,
            color='r',label= "Nota de Alumnos")
plt.title("Notas del Curso de Historia")

plt.xlabel('Codigo de Alumno')
plt.ylabel('Nota del Curso')

# promedio
print(sum(notas_alumnos)/len(notas_alumnos))

# desviacion estandar
import numpy as np
n_a = np.array(notas_alumnos)
print(n_a.std())

# varianza
print(n_a.var())

'''


#print(notas_alumnos)

#plt.show()


import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
x = np.arange(0,360,1)

angle = x*(2*PI/360)
y1 = np.sin(angle)  # Seno
y2 = np.cos(angle)  # Cosemo
y3 = 0.5 + 0.001*x        # Recta con pendiente positiva
y4 = 0.5 - 0.001*x        # Recta con pendiente negativa


fig, ax = plt.subplots()

ax.plot(x, y1, label="Seno")
ax.plot(x, y2, label="Cosemo")
ax.plot(x, y3, label="Recta con pendiente +")
ax.plot(x, y4, label="Recta con pendiente -")
ax.set_xlabel('Grados')
ax.legend()

plt.show()