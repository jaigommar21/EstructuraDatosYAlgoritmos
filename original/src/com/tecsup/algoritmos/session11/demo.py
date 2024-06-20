class BSTNode:
    '''
    Node BST definition
    '''
    def init(self, data):
        self.left = None
        self.right = None
        self.data = data

if __name__ == "__main__":

    nros = [4,5,19,3,5,6,12]
    print(nros)
    print(max(nros))
    print(min(nros))
    print(len(nros))


"""     tree = BSTNode(5)

    tree.left = BSTNode(3)
    tree.left.left= BSTNode(2)
    tree.left.right = BSTNode(4)

    tree.right = BSTNode(7)
    tree.right.left = BSTNode(6)
    tree.right.right = BSTNode(8) """