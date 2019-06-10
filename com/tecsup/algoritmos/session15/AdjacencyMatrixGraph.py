

class Vertex:
    '''getVertex
    Vertex class
    '''
    def __init__(self, node):
        self.id:int = node
        # Mark all nodes unvisited
        self.visited = False

    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def getConnections(self, G):
        #print(type(self.id))
        return G.adjMatrix[G.getVertexIndex(self.id)]

    def getVertexID(self):
        return self.id

    def setVertexID(self, id):
        self.id = id

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)


class Graph:

    '''
    Graph class
    '''
    def __init__(self, numVertices, cost=0):
        #self.adjMatrix = [[-1] * numVertices for _ in range(numVertices)]
        self.adjMatrix \
            = [[-1 for u in range(numVertices)]
                for v in range(numVertices)]
        #print(self.adjMatrix)
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def setVertex(self, vtx :int , id ):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(id)

    def getVertexIndex(self, n):
        for vertxin in range(0, self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                return vertxin
        return (-1)

    def getVertex(self, index):
        return self.vertices[index]

    def addEdge(self, frm: object, to: object, cost: object = 0) -> object:
        if self.getVertexIndex(frm) != -1 and self.getVertexIndex(to) != -1:
            self.adjMatrix[self.getVertexIndex(frm)][self.getVertexIndex(to)] = cost
            # For directed graph do not add this
            self.adjMatrix[self.getVertexIndex(to)][self.getVertexIndex(frm)] = cost

    def getVertices(self):
        vertices = []
        for vertxin in range(0, self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[v].getVertexID()
                    uid = self.vertices[u].getVertexID()
                    edges.append((vid, uid, self.adjMatrix[u][v]))
        return edges


if __name__ == '__main__':
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
    G.printMatrix()
    print(G.getEdges())

    #G.getVertex(2).getConnections(G)
    print(G.getVertex(2).getConnections(G))
    #print(G.getVertexIndex('c'))