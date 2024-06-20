'''
Created on Mar 26, 2020
@author: jgomezm
'''
# Ejercicio  - Crear un cola simple , donde vas
# ingresar 5 valores en forma secuencial : "A","E","I","O","U"
#             ["A","E","I","O","U"]
# recuperar 2 valores de la cola 
#             ["I","O","U"]
# ingresar 3 valores : "1","2","3"
#             ["I","O","U","1","2","3"]
# recuperar 1 valor de la cola 
#             ["O","U","1","2","3"]

# cola vacia
queue = []
print("-------------------------")
print("inicio  -->",queue)

# enQueue 11 : agrega datos a la cola
queue.append(11)
print("-------------------------")
print("enQueue 11 -->",queue)

# deQueue  : recupera datos de la cola 
rd = queue.pop(0)  # el 0 indica la posicion
print("-------------------------")
print("deQueue  -->",queue)
print("data     <--",rd)

# enQueue 12
queue.append(12)
print("-------------------------")
print("enQueue 12 -->",queue)

# enQueue 13
queue.append(13)
print("-------------------------")
print("enQueue 13 -->",queue)

# deQueue  : recupera datos de la cola 
rd = queue.pop(0)  # el 0 indica la posicion
print("-------------------------")
print("deQueue  -->",queue)
print("data     <--",rd)

# enQueue 21
queue.append(21)
print("-------------------------")
print("enQueue 21 -->",queue)

# enQueue 22
queue.append(22)
print("-------------------------")
print("enQueue 22 -->",queue)

# deQueue  : recupera datos de la cola 
rd = queue.pop(0)  # el 0 indica la posicion
print("-------------------------")
print("deQueue  -->",queue)
print("data     <--",rd)
