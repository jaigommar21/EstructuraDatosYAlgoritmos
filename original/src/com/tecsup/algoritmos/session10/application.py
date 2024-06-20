"

((2+4)*(8-9/3)) 
    6 * 5  = 30

 2+4*8-9/3  = 31

        -

   +          /
         
2    *      9    3 

    4  8


248*+93/-






""




from tree import expression as te

indor_raw = input("Input expression => ")
indor = te.adapterExpression(indor_raw)
print(indor)
print(indor.split(" "))
postfix = te.postfixConvert(indor.split(" "))
print(postfix)
rootNode = te.parserPostfixToBinaryTree(postfix.split(" "))
print(rootNode.eval())