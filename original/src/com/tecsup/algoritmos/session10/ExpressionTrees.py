from structure.stack import StackDynamicArray

operatorPrecedence = {
# operator : priority  => exception "(", ")"
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3
}

def parseToken(indor):

    equation = StackDynamicArray() 
    
    tmp = ''
    
    for char in indor:

        if char not in operatorPrecedence:
            if tmp == '':
                tmp = char
            else: 
                tmp = tmp + char
        else:
            if tmp:
                equation.push(tmp)
                tmp = ''        
            equation.push(char)
    
    if tmp != '':
        equation.push(tmp)

    #print(equation.stk)
    
    return equation.stk


def postfixConvert(inorder):
    
    stack = StackDynamicArray()   # Stack

    postfix = StackDynamicArray() 
         
    for element in inorder:
        if element not in operatorPrecedence:
            postfix.push(element)
        else:
            if stack.size() == 0:
                stack.push(element)
            else:
                if element == "(":   # es apertura?
                    stack.push(element)
                elif element == ")": # es cierre?
                    while stack.peek() != "(":  # busca apertura
                        postfix.push(stack.pop())
                    stack.pop()   # elimina apertura?
                elif operatorPrecedence[element] > operatorPrecedence[stack.peek()]:
                    stack.push(element)
                else:
                    while stack.size():
                        if stack.peek() == '(': # es apertura?
                            break
                        postfix.push(stack.pop())
                    stack.push(element)
     
    while stack.size():
        postfix.push(stack.pop())
 
    #print(postfix.stk)
    #return "".join(postfix.stk)
    #return list(postfix) # Support more one digit
    return postfix.stk # Support more one digit

#
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def eval(self):
        #print(eval)

        if self.right is not None and self.left is not None :
            if self.value == '+':
                return self.left.eval() + self.right.eval()
            elif self.value == '-':
                return self.left.eval() - self.right.eval()
            elif self.value == '*':
                return self.left.eval() * self.right.eval()
            elif self.value == '/':
                return self.left.eval() / self.right.eval()
            elif self.value == '^':
                return self.left.eval() ** self.right.eval()
        else:
            return float(self.value)

#
def buildExpressionTree(infix):

    postfix = postfixConvert(infix)

    #print(postfix)

    stack = StackDynamicArray()
 
    for char in postfix:
        
        node = Node(char) 
        
        if char in operatorPrecedence:
            node.right = stack.pop()
            node.left = stack.pop()
        
        stack.push(node)

    return stack.pop()

#################################
# First Case :  (5+3)*6
#
#            *
#
#       +        6
#
#    5     3
#################################
def evalManual():
    opeNodeA = Node(5)
    opeNodeB = Node(3)

    sumNode = Node('+')
    sumNode.left = opeNodeA
    sumNode.right = opeNodeB

    opeNodeC = Node(6)
    mulNode = Node('*')
    mulNode.left = sumNode
    mulNode.right = opeNodeC

    print(mulNode.eval())

# ((5-3)-(6*4)/(4+2)) ^ 2

#################################
# Ejercicio :  (5-3)-(6*4)/(4+2)
#
#             -
#
#      -              / 
#
#   5     3      *          +
#
#             6    4     4    2
#
#################################


#################################
# Second Case : 
#             Function to convert
#             postfix to binary tree
# input : Postfix
# return : Binary Tree
#################################
def parserPostfixToBinaryTree(postfix):

    stack = StackDynamicArray()

    #print(postfix)
    for char in postfix:
        
        node = Node(char)
            
        if char in operatorPrecedence:
            # when char is operator
            node.right = stack.pop()
            node.left = stack.pop()
    
        stack.push(node)

    return stack.pop()


#################################
# Second Case :  Evaluate Postfix
#                espression
#
#  Binary tree :  (5+3)*6
#
#            *
#
#       +        6
#
#    5     3
#
# Indor expression   : (5+3)*6
# Postfix expression : 53+6*
# Prefix expression  : *+536
#################################
def evalPostfixExpression():

    postfix =  "53+6*"
    rootNode = parserPostfixToBinaryTree(postfix)
    res = rootNode.eval()
    print(f"input = {postfix}  | output = {res}")


'''
    EQUATION : ((5-3)-(6-4)/(4+2))^2

                      ^
      
             -                 2
      -            /
    5   3          
               -        +
             6   4   4     2

    53-64-42+/-2^  --> OK

    53-–6–442+/^2  -->
'''

#################################
# Third Case :  Convert indor to 
#               postfix expression
# Indor expression   : (5+3)*6
# Postfix expression : 53+6*
#################################
def convertIndorToPostfixExp():
    indor = "(5+3)*6"
    #indor = "((2*3)+(6/3))" # 23*63/*
    #indor = "((2+4)*(80-9/3))"
    #indor = "((5-3)–(6*4)/(4+2))^2"  # CON ERROR EN EL MENOS 
    #indor = "((5-3)-(6*4)/(4-2))^2"  # FUNCIONA CORRECTAMETNE
    #indor = "2*3^2"  # FUNCIONA CORRECTAMETNE
    indor = parseToken(indor)         # Support more one digit
    postfix = postfixConvert(indor)
    print(f"input = {indor}  | output = {postfix}")

#################################
# Fourth Case :  Evaluate Indor Expression
# Indor expression   : (5+3)*6
#################################
def evalIndorExpression():
    indor = "(5+3)*6"
    #indor = "((2+4)*(0+9*3))"
    #indor = "((5-3)-(6*4)/(4-2))^2"
    #indor = "((2+4)*(80-9/3))"
    #indor = "2*3^2"  # FUNCIONA CORRECTAMETNE
    indor = parseToken(indor) # Support more one digit
    postfix = postfixConvert(indor)
    rootNode = parserPostfixToBinaryTree(postfix)
    print(rootNode.eval())

#################################
# Fifth Case : Input Indor Expression 
#              from Keyboard
# 
#################################
def evalIndorExpressionFromKeyboard():
    indor = input("Input expression => ")
    postfix = postfixConvert(indor)
    rootNode = parserPostfixToBinaryTree(postfix)
    print(rootNode.eval())

#################################
# Main
#################################
if __name__ == '__main__':
    '''
    Este metodo es para 
    '''
    # evalManual()
    # evalPostfixExpression()
    # print(parseToken("((2+4)*(80-9/3))"))
    # convertIndorToPostfixExp()
    evalIndorExpression()
    # evalIndorExpressionFromKeyboard()


'''
Execise 1 :

+ * A B / C D

( (A * B) + ( C / D ) ) 

A B * C D / +

Execise 2 :

* + A B - C / D F

( ( A + B ) * (C - D / F ) ) 

A  B + C D F / - *

Execise 3 :

+ A B 

     +
   A   B 

* + A B + C D

         *
     +       +       
   A   B   C    D


- A / B * C - D E

        - 
     A      /       
         B    *
            C   - 
               D   E

 

Execise 4 :


A B + 

     +
   A   B 

A B + C D + *

         *
     +       +       
   A   B   C    D


A B C D E - * / -

        - 
     A      /       
         B    *
            C   - 
               D   E

'''