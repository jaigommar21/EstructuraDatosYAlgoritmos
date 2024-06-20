'''
Ejemplo de Memory Heap
'''

class Student:
    def __init__(self,name):
        self.name = name

student_1 = Student("Juan")  ## ¿¿¿????
print(student_1.name)


def recursivo(n):
    '''
    Imprime en forma recursiva
    Usa : Stack
    '''
    if n == 0 :
        return
    else:
        n -=1
        print("hola")
        recursivo(n)

i = 4
print(recursivo(i))
#print(type(i))

# <class 'int'>


for i in range(100000000000000):
    student_1 = Student("Juan")  ## Usa la memoria heap
    #i = 4
    print(student_1.name)


recursivo(1)  #  Stack : Pilas


'''
Memory

|--------------------
|  Variables y datos
|
|--------------------
|  Código
|
|--------------------
|  STACK -- aprox 1024
|
|
.
.
.
| 
|  HEAP ---
|--------------------

'''

[3,4,6,81,199,200,12]

# 1.- BST  ( min y max)

# 2.-  Heap Max , Heap Min

# ¿ En que momento consumes memoria ?


















