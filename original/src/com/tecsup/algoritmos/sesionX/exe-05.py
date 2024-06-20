class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):

        if self.right is not None and self.left is not None :

            if self.value == '+':

                return self.left.eval() + self.right.eval()

            elif self.value == '*':

                return self.left.eval() * self.right.eval()

        else:

            return float(self.value)

#################################
# First Case :  (5+7)*13
#
#         *
#     +      6
#   5   3
#################################

## Exercise : (((5+3)*6)-3)/2 

def evalManual():
    
    opeNodeA = Node(5)
    opeNodeB = Node(7)

    sumNode = Node('+')
    sumNode.left = opeNodeA
    sumNode.right = opeNodeB

    opeNodeC = Node(13)
    mulNode = Node('*')
    mulNode.left = sumNode
    mulNode.right = opeNodeC

    print(mulNode.eval())

#
evalManual()
