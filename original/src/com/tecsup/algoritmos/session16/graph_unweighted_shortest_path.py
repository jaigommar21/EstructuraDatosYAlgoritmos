'''
Different type of search in graph

'''

from  graph.impl_adj_list import Vertex, Graph
from  basic.impl_queue import Queue


WITHOUT_DISTANCE = -1

# Un weighted Shortest Path with BFS
def UnweightedShortestPath(g, s):
    source = g.getVertex(s)
    source.setDistance(0)
    source.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(source)
    while (vertQueue.size > 0):
        currentVert = vertQueue.deQueue()
        for nbr in currentVert.getAdjLists():
            if nbr.getDistance() == WITHOUT_DISTANCE:
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)

    for v in g:
        print(source.getId(), " to ", v.getId(), "-->", v.getDistance())

if __name__ == '__main__':
    
    g = Graph()
    g.addVertex('a', WITHOUT_DISTANCE)
    g.addVertex('b', WITHOUT_DISTANCE)
    g.addVertex('c', WITHOUT_DISTANCE)
    g.addVertex('d', WITHOUT_DISTANCE)
    g.addVertex('e', WITHOUT_DISTANCE)
    g.addVertex('f', WITHOUT_DISTANCE)
    g.addVertex('g', WITHOUT_DISTANCE)
    g.addVertex('h', WITHOUT_DISTANCE)
    g.addEdge('a', 'b')
    g.addEdge('b', 'h')
    g.addEdge('b', 'c')
    g.addEdge('c', 'd')
    g.addEdge('c', 'e')
    g.addEdge('h', 'e')
    g.addEdge('e', 'g')
    g.addEdge('e', 'f')

    UnweightedShortestPath(g,"a")
    