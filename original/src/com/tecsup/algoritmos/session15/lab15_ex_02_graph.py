'''
Example of use module and package 
'''

# Import Vertex and Graph class
from  graph.adj_matrix import Vertex, Graph

# Main program
if __name__ == '__main__':

    G = Graph(6)
    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    G.setVertex(4, 'e')
    G.setVertex(5, 'f')
 
    G.addEdge('a', 'e', 10)
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('b', 'e', 40)
    G.addEdge('e', 'd', 50)
    G.addEdge('f', 'e', 60)

    print('Graph matrix:')
    G.printMatrix()

    print('Graph connection:')
    print(G.getEdges())
