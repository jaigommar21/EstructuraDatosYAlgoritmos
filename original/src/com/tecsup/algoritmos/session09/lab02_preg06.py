#################################
# Class Node
#################################
class Node:
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
# Second Case :  53+6*
# input : postfix
# return : Binary Tree
#################################

operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

def parserToTree(postfix):
    stack = []
    for char in postfix:
        if char not in operatorPrecedence:
            # Only accept operands
            node = Node(char)
            stack.append(node)
        else:
            # Only accept operators
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()

#################################
# Second Case :  Evaluate Postfix
#                espression
# Indor expression   : (5+3)*6
# Postfix expression : 53+6*
# Prefix expression  : *+536
#
# INPUT :  Postfix expression
#################################
def evalPostfixExpression(postfix):

    rootNode = parserToTree(postfix)

    print(rootNode.eval())


#################################
# Main
# 
#             *
# 
#        +           6
#     5     3 
#
#################################
if __name__ == '__main__':
    '''
    Este metodo es para 
    '''
    # evalManual()
    postfix =  "53+6*"
    evalPostfixExpression(postfix)
