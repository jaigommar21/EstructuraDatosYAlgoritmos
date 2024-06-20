'''
   Represent Vertex in Graph
'''

import sys


class Vertex:
    
    def __init__(self,key, distance = sys.maxsize):
        self.id = key
        self.adjList = {}

        # Begin : new fields

        # Set distance to infinity for all nodes
        self.distance =  distance
        # Mark all nodes unvisited
        self.visited = False
        # Mark all nodes color with white
        self.color = 'white'
        # Predecessor
        self.previous = None

        # End : new fields

    def addNeighbor(self,nbr,weight=0):
        self.adjList[nbr] = weight

    def getAdjLists(self):
        return self.adjList.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.adjList[nbr]

    # begin : new fields

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    # end : new fields

    #def __str__(self):
    #    return str(self.id) + ' adjList: ' + str([x.id for x in self.adjList])

    def __str__(self):
        return "id:{}  distance:{}".format(self.id, self.distance)

    def __lt__(self, other):
        return self.distance < other.distance

'''
   Represent a Graph
'''
class Graph:

    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self,key, distance = sys.maxsize):
        self.numVertices += 1
        newVertex = Vertex(key, distance)
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

    def printMatrix(self):
        edges = []
        for currentVert in self.vertices.values():
            for nbr in currentVert.getAdjLists():
                curVertID = currentVert.getId()
                nbrID = nbr.getId()
                weight = currentVert.getWeight(nbr)
                print("%s -> %s : %s"%(curVertID, nbrID, weight))
        return edges

    def __iter__(self):
        return iter(self.vertices.values())