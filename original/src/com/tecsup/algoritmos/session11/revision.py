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
            return currentNode.data
        if data < currentNode.data:
            return find(currentNode.left,data)
        else:
            return find(currentNode.right,data)

def findIterative(root, num):
    '''
    Method to find data in BST
    Iterative mode
    :param root:
    :return:
    '''
    currentNode = root
    while currentNode!=num:
        if num == currentNode.data:
            return currentNode.data
        if num < currentNode.data:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
    return None


root=BSTNode(5)
root.left=BSTNode(3)
root.right=BSTNode(7)
root.left.left=BSTNode(2)
root.left.right=BSTNode(4)
root.right.left=BSTNode(6)
root.right.right=BSTNode(8)


print(find(root,7))