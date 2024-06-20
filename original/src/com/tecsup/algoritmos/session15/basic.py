
DEFAULT_VALUE = 0
numVertices = 29
matrix_adj = \
        [ [ DEFAULT_VALUE for u in range(numVertices)] for v in range(numVertices)]

for row in matrix_adj :
     print(row)

"""
     A   B   C   D
A[ [-1,  1, -1, -1],   
B  [-1, -1, -1, -1], 
C  [-1, -1, -1, -1], 
D  [-1, -1, -1, -1]]

"""