"""
Support numbers with several digits
"""
#
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
            elif self.value == '-':
                return self.left.eval() - self.right.eval()
            elif self.value == '/':
                return self.left.eval() / self.right.eval()
            elif self.value == '^':
                return self.left.eval() ** self.right.eval()
            else:
                raise TypeError("Operator not supported : '{}'".format(self.value))
        else:
            return float(self.value)


operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 2
}

def parserEquationToList(indor):
    equation = []
    tmp = ''
    for idx in range(len(indor)):
        char = indor[idx]
        #print(char)
        if char not in operatorPrecedence:
            if idx == (len(indor) - 1): # Last element
                equation.append(tmp + char) # Insert last number
            elif tmp == '':
                tmp = char     
            else: 
                tmp = tmp + char  # Number with several digits
        else:
            if tmp: # First, insert number if exist
                equation.append(tmp)
                tmp = ''        
            equation.append(char) # Insert operator
    return equation


def fromIndorToPostfix(infix):
    stack = []
    postfix = [] 
         
    for char in infix:
        if char not in operatorPrecedence:
            postfix.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack[len(stack) - 1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif operatorPrecedence[char] > operatorPrecedence[stack[len(stack) - 1]]:
                    stack.append(char)
                else:
                    while len(stack) != 0:
                        if stack[len(stack) - 1] == '(':
                            break
                        postfix.append(stack.pop())
                    stack.append(char)
     
    while len(stack) != 0:
        postfix.append(stack.pop())
 
    return list(postfix) # Support more one digit

#
def buildExpressionTree(infix):
    postfix = postfixConvert(infix)

    print(postfix)

    stack = []
 
    for char in postfix:
        if char not in operatorPrecedence:
            node = Node(char)   
            stack.append(node)
        else:
            node = Node(char)
            right = stack.pop()
            left = stack.pop()
            node.right = right
            node.left = left
            stack.append(node)

    return stack.pop()

def parserPostfixToBinaryTree(postfix):

    stack = []
    #print(postfix)
    for char in postfix:
        #print(char)
        if char not in operatorPrecedence:
            # when char is operando
            node = Node(char)
            stack.append(node)
        else:
            # when char is operator
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack.pop()

#################################
# Main
#################################
if __name__ == '__main__':

    #indor = "(5+3)-6"
    #indor = "((2+4)*(0+9*3))"
    indor= "((5-3)-(65*4)/(400+2))^2"
    #indor="((5-3)-(6*4)/(4+2))^2"
    #indor="2+4*8-9/3"
    #indor = "((5-3)-(6-40)/(4+21))^12"
    print(indor)
    indor = parserEquationToList(indor) # Support more one digit
    postfix = fromIndorToPostfix(indor)
    #print(postfix)
    rootNode = parserPostfixToBinaryTree(postfix)
    print(rootNode.eval())