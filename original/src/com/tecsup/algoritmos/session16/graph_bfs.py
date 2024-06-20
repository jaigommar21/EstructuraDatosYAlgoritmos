'''
Different type of search in graph

'''

from  graph.impl_adj_list import Vertex, Graph
from  basic.impl_queue import Queue

# Color white : Node is not visit
# Color black : Node was visited
# Color gray : Node is being visited


# BFS : Breadth First Search
def BFSTraversal(g, s):
    
    start = g.getVertex(s)
    start.setDistance(0)
    start.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(start)

    while (vertQueue.size > 0):
        currentVert = vertQueue.deQueue()
        print(currentVert.getId())
        for nbr in currentVert.getAdjLists():
            if (nbr.visited == False): # unmarked
                nbr.visited = True # marked
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)
        currentVert.visited = True # marked


def BFS(g):
    for v in g:
        #if (v.getColor() == 'white'):  # unmarked
        if (v.visited == False):  # unmarked
            BFSTraversal(g, v.getId())


if __name__ == '__main__':
    
    g = Graph()
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addVertex('g')
    g.addVertex('h')
    g.addEdge('a', 'b', 1)
    g.addEdge('b', 'h', 1)
    g.addEdge('b', 'c', 1)
    g.addEdge('c', 'd', 1)
    g.addEdge('c', 'e', 1)
    g.addEdge('h', 'e', 1)
    g.addEdge('e', 'g', 1)
    g.addEdge('e', 'f', 1)
    print('Graph data:')
    for row in g.getEdges():
        print("%s -> %s : %s"%(row[0], row[1], row[2]))

    # Search
    BFS(g)

    # Where start?
    for v in g: 
        if v.previous == None :
            print("START IN : {} ".format(v.id)) 

    # Print
    for v in g: 
        print("id:[{}] distance:[{}]".format(v.id, v.distance))
    
