class Usuario:
    '''
    Node BST definition
    '''
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad


class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


if  __name__ == '__main__':

    root = BSTNode(4)
    root.left = BSTNode(2)
    root.right = BSTNode(14)
    root.right.left = BSTNode(8)

    print(root)

    root = BSTNode(Usuario(14,"Susan",23))

    root.left = BSTNode(8)
    root.left.left = BSTNode(2)
    root.left.rigt = BSTNode(10)
    
    root.right = BSTNode(25)
    root.right.left = BSTNode(20)
    root.right.rigth = BSTNode(33)

    print(root)

    


    pass

