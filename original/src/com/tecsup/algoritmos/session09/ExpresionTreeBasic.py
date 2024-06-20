#
########################################
#       Expression Tree
########################################
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):

        if self.left is not None and self.right is not None :
            if self.value == '+':
                return self.left.eval() + self.right.eval()
            elif self.value == '*':
                return self.left.eval() * self.right.eval()

        else:
            return float(self.value)


#################################
# First Case :  (5+3)*6
#
#         *
#     +      6
#   5   3
#################################
if __name__ == '__main__':

    opeNodeA = Node(5)
    opeNodeB = Node(3)
    opeNodeC = Node(6)

    sumNode = Node('+')
    sumNode.left = opeNodeA
    sumNode.right = opeNodeB

    mulNode = Node('*')
    mulNode.left = sumNode
    mulNode.right = opeNodeC

    print(mulNode.eval())

    """
    equation = Node("*")
    equation.left = Node('+')
    equation.right = Node(6)
    equation.left.left = Node(5)
    equation.left.right = Node(3)

    print(equation.eval())
    """


# Ejercicio  :  ( ( 20 + 4) * 2  + 5)

# Ejercicio  :  ( ( 2 ** 3 + 4) * (5 - 3)  + 5 )  / 2 )
