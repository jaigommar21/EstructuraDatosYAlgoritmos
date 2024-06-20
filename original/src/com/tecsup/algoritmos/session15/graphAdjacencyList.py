'''

'''

'''
   Represent Vertex in Graph
'''
class Vertex:
    
    def __init__(self,key):
        self.id = key
        self.adjList = {}

    def addNeighbor(self,nbr,weight=0):
        self.adjList[nbr] = weight

    def getAdjLists(self):
        return self.adjList.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.adjList[nbr]

    def __str__(self):
        return str(self.id) + ' adjList: ' + str([ f"{key.id}:{value}" for key,value in self.adjList.items()])


'''
   Represent a Graph
'''
class Graph:

    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

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
        self.vertices[f] \
              .addNeighbor(self.vertices[t], 
                            weight)

    def getVertices(self):
        return self.vertices.keys()

    def getEdges(self):
        edges = []
        for v in self.vertices.values():
            for w in v.getAdjLists():
                vid = v.getId()
                wid = w.getId()
                edges.append((vid, wid, 
                           v.getWeight(w)))
        return edges

    #def __contains__(self,n):
    #    return n in self.vertList

    #def __iter__(self):
    #    return iter(self.vertList.values())



'''
if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a', 'b', 4)
    G.addEdge('a', 'c', 1)
    G.addEdge('c', 'b', 2)
    G.addEdge('b', 'e', 4)
    G.addEdge('c', 'd', 4)
    G.addEdge('d', 'e', 4)

    print('Graph data:')
    print(G.getEdges())

#'''

if __name__ == '__main__':

    g = Graph()

    for i in range(6):  g.addVertex(i)

    #print(g.vertList)

    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    """
    for v in g.vertices.values():
        #print(f"vertice = {v}")
        
         for w in v.getAdjLists():
            # print(f" {w} ")
            print(f" {v.getId()} -> {w.getId()}:{v.getWeight(w)}")
            #print("( %s , %s , %s )" % (v.getId(), w.getId(), v.getWeight(w)))
    """
        
    for v in g.vertices.values():
            print(f"vertice = {v.getId()}")

            for w in v.getAdjLists():
                print(f" {v.getId()} -> {w.getId()}:{v.getWeight(w)}")

#'''