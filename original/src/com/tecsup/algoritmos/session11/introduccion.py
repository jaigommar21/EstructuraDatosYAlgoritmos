
var = 1  # Contenido dentro del concepto
         # de un arbol binario

#         1 
#

var = [1,3] # Una lista esta contenido dentro
            # del concepto de un arbol binario

#         1 
#          \
#           3


#          1 
#        /  \
#       2    3


#
#          1
#        /  \
#       /    \
#     2        3
#    /  \     / \
#   4    5   6   7
#

#  ¿ Como buscar el valor de 5 ?
#  LDR , LRD , DLR

# LDR : 4 - 2 - 5 - 1 - 6 - 3 - 7  = 3 pasos   
# LRD : 4 - 5 - 2 - 6 - 7 - 3 - 1  = 2 paso
# DLR : 1 - 2 - 4 - 5 - 3 - 6 - 7  = 4 pasos

# ¿ Cómo saber cual recorrido usar?
# Busco el 5

        #          4
		# 	    / \
		#        /   \	 
		#      2      6
		#     / \    / \ 
		#    1   3  5   7 



#    1 dato  --> 1 paso (1 segundo) como maximo  ( 1 nivel )


#    3 datos --> 2 pasos (2 segundos) como maximo ( 2 niveles )


#    7 datos --> 3 pasos (3 segundos) como maximo ( 3 niveles )


#   15 datos --> 4 pasos (4 segundos) como maximo ( 4 niveles )

#   31 datos --> 5 pasos (5 segundos) como maximo ( 5 niveles )

#   63 datos --> 6 pasos (6 segundos) como maximo ( 6 niveles )

#  127 datos --> 7 pasos (7 segundos) como maximo ( 7 niveles )

#  255 datos --> 8 pasos (8 segundos) como maximo ( 8 niveles )

#  511 datos --> 9 pasos (9 segundos) como maximo ( 9 niveles )

# 1023 datos --> 10 pasos (10 segundos) como maximo ( 10 niveles )

# 2043 datos --> 11 pasos (11 segundos) como maximo ( 11 niveles )

# 65535 datos , solo necesito 16 segundos

# 1048575 datos ¿Cuanto es el tiempo máximo para encontrar un dato?

# Rpta : 20 segundos


#
#                                          nivel
#   numero maximo de datos soportados =  2     -  1
#   
#


# Convertir a un BST : 
#       1,2,3,4,5,6,12,13,14,15,7,8,9,10,11
#
#                   8
# 				  /    \	 
# 			     /       \
# 		        /          \	 
# 		       4            12
# 		     /  \         /    \ 
# 		   2     6     10       14 
#         / \    / \    / \    /  \ 
#        1   3  5   7  9  11  13  15


# Ejercicio

#listado = [1,40,50,45,23]

listado = [1,2,3,4,5,6,12,13,14,15,7,8,9,10,11]

print(max(listado)) # BST
print(min(listado)) # BST
print(sum(listado)) # ¿?

