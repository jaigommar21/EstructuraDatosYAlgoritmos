'''
Created on April 30, 2020
@author: jgomezm
@version: 1.0
'''


'''
Binary Tree

                     Root
                      |
            ----------------------
            |                     | 
           Left                  Right   

'''

tree = ["Root","Left","Right"] # No es correcto

# ???


'''
Binary Tree : Left and Right are empty

                     Root

'''

tree = ["Root", [], [] ] # es un nodo

# posicion 0 : la raiz
# posicion 1 : la rama derecha
# posicion 2 : la rama izquierda

'''
    4

'''
var = 4   #  

tree = [4, [] , []]

'''
Binary Tree : Right is empty

                     Root
                      |
            ----------------------
            |                      
           Left                    

'''
tree = ["Root", 
            ["Left", [], [] ],
            [] 
       ]



left = ["Left", [], [] ]

tree = ["root", left , []]

'''
Binary Tree : Left is empty

                     Root
                      |
            ----------------------
                                 | 
                                Right   

'''

tree = ["Root", 
            [ ],
            ["right", [], []] 
       ]


right = ["Right", [], [] ]

tree = ["Root", [] , right]

tree = ["Root", 
            [],
            ["Right", [], []] 
       ]



'''
Generic Tree

                            Continents
                                 |
            ---------------------------------------------   
            |                    |                      |
          America             Europe                  Asia     
            |                    |                      |
      --------------         ---------         --------------------
      |     |      |         |       |         |        |         | 
    Peru  Chile Ecuador    Spain  France     China  Singapore  Malaysia

'''

tree = [ "Continents", #root
            ["America",
                ["Peru","Chile","Ecuador"]
            ],     
            ["Europe",
                ["Spain","France"]
            ],
            ["Asia",
                ["China","Singapore","Malaysia"]
            ]
        ]

print("------------------------------------------------------")
#print(tree)
print("root = ",tree[0])
print("left sub tree = ",tree[1])
print("center sub tree = ",tree[2])
print("right sub tree = ",tree[3])

'''
Binary Tree

                    Numero
                      |
            ----------------------
            |                     | 
           Par                   Impar   
            |                     | 
      ------------          -----------  
      |          |          |         |   
    <= 100      >100       <= 50     > 50  

'''



decision_tree = [
                    "Numero",  # root
                        ["Par",    # left sub tree
                            ["<= 100" , [] , [] ] , # left left sub tree
                            ["> 100"  , [] , [] ]   # right left sub tree
                        ],       
                        ["Impar",  # right sub tree 
                            ["<= 50" , [] , [] ] ,  # left right sub tree
                            ["> 50"  , [] , [] ]    # right right sub tree
                        ]         
                ]

                

print("------------------------------------------------------")
#print(decision_tree)
print("root = ",decision_tree[0])
print("left sub tree = ",decision_tree[1])
print("right sub tree = ",decision_tree[2])

print("------------------------------------------------------")
binary_tree = ["root",
                ["left sub tree",[],[]],
                ["right sub tree",[],[]]
              ]
print("root  = ",binary_tree[0])
print("left  = ",binary_tree[1])
print("right = ",binary_tree[2])

print("------------------------------------------------------")
binary_tree_1 = ["root",[],[]]
print("root  = ",binary_tree_1[0])
print("left  = ",binary_tree_1[1])
print("right = ",binary_tree_1[2])

print("------------------------------------------------------")
binary_tree_1 = ["root",[],[]]
left_sub_tree = binary_tree_1.pop(1)
print("root  = ",binary_tree_1[0])
#print("left  = ",binary_tree_1[1])
print("left_sub_tree  = ",left_sub_tree)
#print("right = ",binary_tree_1[2])
print("right = ",binary_tree_1[1])

print("-----------------------------------------------------")
binary_tree_1 = ["root",[],[]]

print("")
print("root  = ",binary_tree_1[0])
print("left  = ",binary_tree_1[1])
print("right = ",binary_tree_1[2])

left_sub_tree = binary_tree_1.pop(1)
binary_tree_1.insert(1,["left sub tree", [],[]])

right_sub_tree = binary_tree_1.pop(2)
binary_tree_1.insert(1,["right sub tree", [],[]])

print("")
print("root  = ",binary_tree_1[0])
print("left  = ",binary_tree_1[1])
print("right = ",binary_tree_1[2])


'''
Representar :  (5+4)*(2-1)
                      *
                      |
            ----------------------
            |                     | 
            +                     -   
            |                     | 
      ------------          -----------  
      |          |          |         |   
      5          4          2         1 

             --------------     ----------- 
  Input ===> | Preprocess | ==> | Process | ==> Output    
             --------------     -----------
(5+4)*(2-1)   ConvertToTree       Calculate     Data

 example.py      compiler         execute       console


Representar :  ((5+4)*(20-1))*(4-2)

Representar :  ((5+10)*(2-1))*((4-2)/(5-2))

'''


'''
Binary Tree

                  Estudiante
                      |
            ----------------------
            |                     | 
         Aprobado            Desaprobado  
     

'''
print("-----------------------------------------------------")
                   #    0 :nodo     1 : left  2 : right 
student_bin_tree = ["Estudiante" ,    []      ,    []]

left_sub_tree = student_bin_tree.pop(1) 
# student_bin_tree[1] = ["Aprobado"   ,[],[]]
student_bin_tree.insert(1,["Aprobado"   ,[],[]])

right_sub_tree = student_bin_tree.pop(2)
student_bin_tree.insert(2,["Desaprobado",[],[]])

print("root  = ",student_bin_tree[0])
print("left  = ",student_bin_tree[1])
print("right = ",student_bin_tree[2])


'''
Binary Tree

                  Estudiante
                      |
            ----------------------
            |                     | 
         Aprobado            Desaprobado  
            |                     | 
       -----------          -------------    
       |          |         |           |
    Excelente   Bueno    Regular    Deficiente 

'''

print("-----------------------------------------------------")

student_bin_tree = ["Estudiante" ,[],[]]

left_sub_tree = student_bin_tree.pop(1)
student_bin_tree.insert(1,["Aprobado" ,[],[]])

right_sub_tree = student_bin_tree.pop(2)
student_bin_tree.insert(2,["Desaprobado",[],[]])

left_sub_tree = student_bin_tree.pop(1)
left_left_sub_tree = left_sub_tree.pop(1)
left_sub_tree.insert(1,["Excelente" ,[],[]])
right_left_sub_tree = left_sub_tree.pop(2)
left_sub_tree.insert(2,["Bueno" ,[],[]])
student_bin_tree.insert(1,left_sub_tree)

right_sub_tree = student_bin_tree.pop(2)
left_right_sub_tree = right_sub_tree.pop(1)
right_sub_tree.insert(1,["Regular" ,[],[]])
right_right_sub_tree = right_sub_tree.pop(2)
right_sub_tree.insert(2,["Deficiente" ,[],[]])
student_bin_tree.insert(2,right_sub_tree)

print("root        = ",student_bin_tree[0])
print("left        = ",student_bin_tree[1])
print("left left   = ",student_bin_tree[1][1])
print("right left  = ",student_bin_tree[1][2])
print("right       = ",student_bin_tree[2])
print("left right  = ",student_bin_tree[2][1])
print("right right = ",student_bin_tree[2][2])







"""
Example implementation with list

Binary Tree

                    Numero
                      |
            ----------------------
            |                     | 
           Par                   Impar   
                                
"""
arbol = [ "Numero" , 
                    ["Par"  , [] ,[] ] , 
                    ["Impar", [] ,[] ]
        ]

print("LEFT --> " , arbol[1])

