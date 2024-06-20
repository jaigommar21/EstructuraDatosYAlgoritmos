'''
  getVertex
  Vertex class
'''

'''
   Represent Vertex in Graph
'''
class Vertex:

    def __init__(self, node):
        self.id = node

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

'''
   Represent a Graph
'''
DEFAULT_COST = 0
NOT_EXIST = -1

class Graph:

    def __init__(self, numVertices, cost = DEFAULT_COST ):
        '''
         self.adjMatrix : matrix adjunta del grafo
         self.numVertices : numero de vertices o nodos
         self.vertices : listado de las instancias de los nodos
        '''
        self.adjMatrix \
            = [[ cost for u in range(numVertices)]
                for v in range(numVertices)]

        self.numVertices = numVertices
        
        self.vertices = [ Vertex(i) for i in range(0,numVertices)]
        

    def setVertex(self, key_vertex , id ):
        if 0 <= key_vertex < self.numVertices:
            self.vertices[key_vertex].setId(id)

    def getKeyVertex(self, search_id):
        for key in range(0, self.numVertices):
            if search_id == self.vertices[key].getId():
                return key
        return NOT_EXIST

    def getVertex(self, index):
        return self.vertices[index]

    def addEdge(self, from_, to_, cost = 0):

        key_from_ = self.getKeyVertex(from_)
        key_to_ = self.getKeyVertex(to_)

        if key_from_ != NOT_EXIST and key_to_!= NOT_EXIST :

            self.adjMatrix[key_from_][key_to_] = cost
        
            ''' For directed graph do not add this'''
            # self.adjMatrix[key_to_][key_from_] = cost

    def getIdsVertice(self):
        vertices = [ vertex.getId() for  vertex in self.vertices  ]     
        return vertices

    def printMatrix(self):
        for row in self.adjMatrix: print(row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] != DEFAULT_COST:
                    vid = self.vertices[v].getId()
                    uid = self.vertices[u].getId()
                    edges.append((vid, uid, self.adjMatrix[u][v]))
        return edges

'''
vertices [ vertice 0 , vertice 1, vertice 2]

   vertice 0
    --------
    | Lima |
    --------

   vertice 1
    --------
    | Ica |
    --------

   vertice 2
    ------------
    | Arequipa |
    ------------

'''
if __name__ == '__main__':

    ''' Codigo para clase de teoria
    nro_vertex = 3
    G = Graph(nro_vertex)

    # Configuracion de vertices
    G.setVertex(key_vertex=0, id='Lima')
    G.setVertex(key_vertex=1, id='Ica')
    G.setVertex(key_vertex=2, id='Arequipa')

    # Creacion de aristas
    G.addEdge(from_='Lima', to_='Ica', cost=2)
    G.addEdge(from_='Ica', to_='Arequipa', cost=2)
    G.addEdge(from_='Lima', to_='Arequipa', cost=3)
    
    #'''

    '''
           a   b   c   d   e   f
     a   [-1, -1, 20, -1, 10, -1]
     b   [-1, -1, -1, -1, 40, -1]
     c   [-1, 30, -1, -1, -1, -1]
     d   [-1, -1, -1, -1, -1, -1]
     e   [-1, -1, -1, 50, -1, -1]
     f   [-1, -1, -1, -1, 60, -1]

           a   b   c   d   e   f
     a   [-1, -1, 20, -1, 10, -1]
     b   [-1, -1, 30, -1, 40, -1]
     c   [20, 30, -1, -1, -1, -1]
     d   [-1, -1, -1, -1, 50, -1]
     e   [10, 40, -1, 50, -1, 60]
     f   [-1, -1, -1, -1, 60, -1]
    
    '''


    #''' Codigo para laboratorio
    G = Graph(6)
    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    G.setVertex(4, 'e')
    G.setVertex(5, 'f')
    print('Graph data:')
    G.addEdge('a', 'e', 10)
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('b', 'e', 40)
    G.addEdge('e', 'd', 50)
    G.addEdge('f', 'e', 60)
    #'''

    G.printMatrix()
    print(G.getEdges())

"""
      a  b  c    d   e  f
   a [0, 0, 20,  0, 10, 0]
   b [0, 0,  0,  0, 40, 0]
   c [0, 30, 0,  0,  0, 0]
   d [0, 0,  0,  0,  0, 0]
   e [0, 0,  0, 50,  0, 0]
   f [0, 0,  0,  0, 60, 0]

"""