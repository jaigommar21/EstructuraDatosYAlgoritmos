'''
Created on Mar 10, 2019

@author: jgomezm
'''

class QueueSimpleArray:

    def __init__(self, limit = 5):
        self.que = []
        self.limit = limit
        self.front = None  # apunta a la posicion
                           # del elemento que va hacer 
                           # atendido en la cola

        self.rear = None   # apunta a la posicion
                           # del ulitmo elemento ingresado 
                           # en la cola   
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, item):
        if self.size >= self.limit :
            print('Queue Overflow..!')
            return -1
        else:
            self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1
        #print('Queue after enQueue',self.que)

    def deQueue(self):
        
        #print('Queue before deQueue',self.que)

        if self.size <= 0:
            print('Queue Underflow....!')
            return -1
        else:
            value = self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size -1
            #print('Queue after deQueue', self.que)

        return value

    def queueRear(self):
        if self.rear is None:
            print('Sorry, the queue is empty..!')
            #raise IndexError
            return -1
        return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            print('Sorry, the queue is empty')
            #raise IndexError
            return -1
        return self.que[self.front]

    def getSize(self):
        return self.size

    def getQue(self):
        return self.que


#################################
# Main
#################################
if __name__ == '__main__':

    # Execution
    que = QueueSimpleArray()

    print("--------------------------------")
    que.enQueue("first")
    print("Que   --> " , que.getQue())
    print("Front --> " , que.queueFront())
    print("Rear  --> " , que.queueRear())

    print("--------------------------------")
    que.enQueue("second")
    print("Que   --> " , que.getQue())
    print("Front --> " , que.queueFront())
    print("Rear  --> " , que.queueRear())

    print("--------------------------------")
    que.deQueue()
    print("Que   --> " , que.getQue())
    print("Front --> " , que.queueFront())
    print("Rear  --> " , que.queueRear())

    print("--------------------------------")
    que.deQueue()
    print("Que   --> " , que.getQue())
    print("Front --> " , que.queueFront())
    print("Rear  --> " , que.queueRear())



"""

que.deQueue()
que.deQueue()
que.deQueue()
que.deQueue()
print("Que   --> " , que.getQue())
print("Front --> " , que.queueFront())
print("Rear  --> " , que.queueRear())
"""


## Ejercicio  : obtener el valor desencolado
##              al llamar al metodo deQueue()
## rd = que.deQueue()
##    
##  rd deberia almacenar el valor desencolado



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
print("--------------------------------")
que.deQueue()
print("Que   --> " , que.getQue())
print("Front -->" , que.queueFront())
print("Rear --> " , que.queueRear())
'''



'''

- Verificar que al desencolar una cola vacia sale 
  un error....!

- Verificar que al momento de encolar una cola llena sale 
  un error....!

'''