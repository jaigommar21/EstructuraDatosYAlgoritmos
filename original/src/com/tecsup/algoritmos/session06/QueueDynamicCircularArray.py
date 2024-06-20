'''
Created on Mar 10, 2019

@author: jgomezm
@version: 1.2 23/04/2020

'''

# Ejercicio  - Crear un cola dinamica , donde vas
# ingresar 5 valores en forma secuencial : "A","E","I","O","U"
#             ["A","E","I","O","U"]
# recuperar 2 valores de la cola 
#             ["I","O","U"]
# ingresar 3 valores : "1","2","3"
#             ["I","O","U","1","2","3"]
# recuperar 1 valor de la cola 
#             ["O","U","1","2","3"]


class QueueDynamicCircularArray(object):

    def __init__(self, limit = 2):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, item):
        if self.size >= self.limit :
            self.resize()
        self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1
        print('Queue after enQueue',self.que)

    def deQueue(self):
        if self.size <= 0:
            print('Queue Underflow....!')
            return 0
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            
            print('Queue after deQueue', self.que)

    def queueRear(self):
        if self.rear is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            print('Sorry, the queue is empty')
            raise IndexError
        return self.que[self.front]

    def getSize(self):
        return self.size

    def resize(self):
        newQue = list(self.que)
        self.que = newQue
        self.limit = 2 * self.limit
        
    def insize(self):
        newQue = list(self.que)
        self.limit = int(self.size / 2)
        self.que = newQue


    def getQue(self):
        return self.que

    def getLimit(self):
        return self.limit

def print_details(que):
    print("Que    --> " , que.getQue())
    print("Front  --> " , que.queueFront())
    print("Rear   --> " , que.queueRear())
    print("Limit  --> " , que.getLimit())
    print("Size   --> " , que.getSize())

"""
# Execution
que = QueueDynamicCircularArray()

data = ["first","second","third","fourth",
        "fifth","sixth","seventh","eighth"]

for item in data:
    print("--------------------------------")
    que.enQueue(item)
    print_details(que)  # Imprimr details
    

for i in range(1,7 + 1 ): # Un ciclo de 7 repeticiones
    print("--------------------------------")
    que.deQueue()
    print_details(que)

"""

'''
Crear un método para reducir el limite a 
la mitad si el doble del valor del size es
menor o igual al valor del limite

'''

"""
print("--------------------------------")
que.deQueue()
print_details(que)


print("--------------------------------")
que.deQueue()
print_details(que)

"""

# Ejercicio  : obtener el valor desencolado
#              al llamar al metodo deQueue()
# rd = que.deQueue()
#    
#  rd deberia almacenar el valor desencolado


'''
ESCENARIO 1 :
-------------

 COLA :         []
 POSICION :     None 
 front = None
 rear  = None

ESCENARIO 2 :
-------------

 COLA :         ["first"]
 POSICION :         0
 front = 0
 rear  = 0

ESCENARIO 3 :
-------------

 COLA :         ["first", "second"]
 POSICION :         0         1
 front = 0
 rear  = 1

'''


'''

- Verificar que al desencolar una cola vacia sale 
  un error....!

- Verificar que al momento de encolar una cola llena NO sale 
  un error al sobrepasar el limite de la cola !

'''


''' 
Ejercicio adicional a la guia de laboratorio:
---------------------------------------------

Al abrir la agencia de un banco , ingresan las
siguiente personas en orden para ser atendidos

Juan Diaz   --> Cliente del Banco
Pedro Garcia
Eduardo Marquez
Julissa Palacios
Juan Acosta
Humberto Leon --> Cliente del Banco
Marisol Aguirre
Pedro Quiroz
Roberto Enciso --> Cliente del Banco
Ana Vargas
Juan Rulfo
Edson de la Cruz

1.- Suponiendo que hay 2 colas, uno para clientes
del banco y otra para no clientes, representar
las 2 colas del banco

2.- Qué clientes se atienden antés y después de 
Roberto Enciso si por cada cliente del banco se 
deben atender 3 clientes que no son del banco, 
considere que solo hay una persona de atención
en el banco

'''

#################################
# Mainp
#################################
if  __name__ == "__main__":

    # Execution
    que = QueueDynamicCircularArray()

    data = ["Jaime","Marisol","Juan","Silvia"]

    for item in data:
        print("--------------------------------")
        que.enQueue(item)
        print("Que    --> " , que.getQue())
        print("Front  --> " , que.queueFront())
        print("Rear   --> " , que.queueRear())
        print("Limit  --> " , que.getLimit())
        print("Size   --> " , que.getSize())

    print("--------------------------------")
    que.deQueue()
    print("Que    --> " , que.getQue())
    print("Front  --> " , que.queueFront())
    print("Rear   --> " , que.queueRear())
    print("Limit  --> " , que.getLimit())
    print("Size   --> " , que.getSize())










