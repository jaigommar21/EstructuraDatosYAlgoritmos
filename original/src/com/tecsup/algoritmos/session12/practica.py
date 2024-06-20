import random
import time

class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def find(root, data):
    '''
    Method to find data in BST
    Rparam root:
    :return:
    '''
    currentNode = root

    if currentNode == None:
        return None
    else:
        if data == currentNode.data:
            return currentNode
        if data < currentNode.data:
            return find(currentNode.left,data)
        else:
            return find(currentNode.right,data)


def insertNode(root, node):

    '''
    Insert a node in BST
    '''
    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)
    

def buildBSTFromArray(list):
    '''
    Build Binary Search Tree
    from Array
    :return:
    '''
    root = None

    for item in list:
        if list.index(item) == 0:
            root = BSTNode(item)
        else:
            insertNode(root, BSTNode(item))
    return root

def create_data(filename):
    data = open(filename, "w")
    for i in range(1000):
        number = random.randrange(1, 50000)
        data.write(str(number) + "\n")

def read_data(filename):        
    data = open(filename, "r")
    lines = data.readlines()
    numeros = []
    for line in lines : numeros.append(int(line))
    return numeros


if __name__ == "__main__":    
    create_data("datos.txt")
    nros = read_data("datos.txt")
    print(len(nros))     
    bst = buildBSTFromArray(nros)
    index_max_value = nros.index(max(nros))
    index_min_value = nros.index(min(nros))
    for idx in [100, 500, 900, index_min_value, index_max_value]:
        print("-"*50)     
        print("---> Buscando :", nros[idx])     
        begin_time = time.perf_counter_ns()
        nro = find(bst, nros[idx])
        end_time = time.perf_counter_ns()
        delay_time = end_time - begin_time
        print("Tiempo empleado ", delay_time , "mcs")
        print(nro)
