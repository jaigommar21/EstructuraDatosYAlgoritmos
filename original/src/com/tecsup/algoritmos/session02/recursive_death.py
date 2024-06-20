'''
Created on Mar 19, 2021
@author: jgomezm
'''
'''
# recursive code
def imprimir(msg): 
    print(msg)
    imprimir(msg)
'''
# iterative code
def imprimir(msg):
    while True:
        print(msg)

if __name__=="__main__":
    imprimir("Hello World ...!")