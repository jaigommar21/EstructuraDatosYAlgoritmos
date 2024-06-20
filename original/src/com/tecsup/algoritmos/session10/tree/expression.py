
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
        else:
            return float(self.value)


#################################
# function : parserPostfixToBinaryTree 
# input : postfix expression
# return : binary Tree
#################################
def parserPostfixToBinaryTree(postfix):

    stack = []
    
    for char in postfix:
        
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
# function : postfixConvert
# input : indor expression
# return : postfix expression
#################################
operatorPrecedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}
 
def postfixConvert(infix):
    stack = []
    postfix = [] 
         
    for char in infix:
        #print(char)
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
 
    return " ".join(postfix)

#
#
#
operatorReplace = {
    '(' : ' ( ',
    ')' : ' ) ',
    '+' : ' + ',
    '-' : ' - ',
    '*' : ' * ',
    '/' : ' / ',
}
def adapterExpression(in_exp):
    for key, value in operatorReplace.items():
       in_exp = in_exp.replace(key, value)
    return " ".join(in_exp.split())