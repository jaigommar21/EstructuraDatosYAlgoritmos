'''
   Represent Vertex in Graph
'''
class Vertex:
    
    def __init__(self,id):
        self.id = id
        self.adjList = {}

    def addNeighbor(self,nbr_vertex,weight=0):
        self.adjList[nbr_vertex] = weight

    def getWeightByNbr(self,nbr_vertex):
        return self.adjList[nbr_vertex]

    def getVertexsOfAdjList(self):
        return self.adjList.keys()

    def __str__(self):
        return str(self.id) + ' adjList: ' + str([ f"{key.id}:{value}" for key,value in self.adjList.items()])



'''
   Represent a Graph
'''
class Graph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def addVertex(self,key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def addEdge(self, f, t, weight = 0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], weight)

    def getKeysOfVertices(self):
        return self.vertices.keys()

    def getEdges(self):
        edges = []
        for v in self.vertices.values():
            for w in v.getAdjLists():
                edges.append((v.id, w.id, v.getWeight(w)))
        return edges