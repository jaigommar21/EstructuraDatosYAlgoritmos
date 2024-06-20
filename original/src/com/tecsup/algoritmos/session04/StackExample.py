'''
Created on Mar 26, 2020
@author: jgomezm
'''

# Ejercicio  - Crear un pila simple , donde vas
# a ingresar 5 valores : "A","E","I","O", "U"
# recuperar 2 valores 
# ingresar  3 valores : "1","2","3"
#  ["A","E","I","1","2","3"]

# pila vacia
stack = []
print("-------------------------")
print("inicio  -->",stack)

# ejecuta un "push" 11 : agrega datos a la pila
stack.append(11)
print("-------------------------")
print("push 11 -->",stack)

# pop  : recupera datos de la pila 
rd = stack.pop()
print("-------------------------")
print("pop     -->",stack)
print("data    <--",rd)

# push 12
stack.append(12)
print("-------------------------")
print("push 12 -->",stack)

# push 13
stack.append(13)  # top apunta a la posicion 0
print("-------------------------")
print("push 13 -->",stack)


# pop 
rd = stack.pop()
print("-------------------------")
print("pop     -->",stack)
print("data    <--",rd)

'''

# push 21
stack.append(21)
print("-------------------------")
print("push 21 -->",stack)

# push 22
stack.append(22)
print("-------------------------")
print("push 22 -->",stack)

# pop 
rd = stack.pop()
print("-------------------------")
print("pop     -->",stack)
print("data    <--",rd)


'''