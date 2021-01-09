import random
import bisect 
from operator import attrgetter
from Graph import Graph

selectedEdges = []
nodesReached = []
availableEdges = []


def prim(graph):
    graphSize = len(graph.nodes)
    print("PRIM'S ALGORITHM : " + str(graphSize))
    currentVertexIndex = random.randint(0, len(graph.nodes)-1)#RANDOM
    print("Initial Vertex = " + str(currentVertexIndex))

    currentNode = graph.nodes[currentVertexIndex]

    while(len(nodesReached) < graphSize):
        newNodeReached(graph, currentNode)
        
        printNodesReached()
        printAvailableEdges()

        if(len(availableEdges) > 0):
            bestAvailableEdge = getBestAvailableEdge()
            #print("Lowest available edge: " + str(bestAvailableEdge.weight) + " to node " + str(bestAvailableEdge.otherNode.id))
            currentNode = bestAvailableEdge.otherNode
        

        
    

    #printNodesReached()
    


    

def newNodeReached(graph, newNode):
    #Remove every edge on other nodes that leads to the reached node
    for node in graph.nodes:
        for edge in graph.nodes[node.id].connectedEdges:
            if(edge.otherNode.id == newNode.id):
                graph.nodes[node.id].connectedEdges.remove(edge)
    print("-----------------UPDATED GRAPH-----------------")
    for node in graph.nodes:
        for edge in graph.nodes[node.id].connectedEdges:
            print("Node " + str(node.id) + ", edge " + str(edge.otherNode.id))
    print("-----------------------------------------------")
    
    #Remove every edge on "availableEdges" that leads to the reached node
    availableEdges[:] = [edge for edge in availableEdges if not (edge.otherNode == newNode)]

    #Add the new edges from the new node to the "availabreEdges" vector
    for edge in newNode.connectedEdges:
        bisect.insort(availableEdges, edge)

    #Add new node to "nodesReached" vector
    nodesReached.append(newNode)

def getBestAvailableEdge():
    if(len(availableEdges) > 0):
        return availableEdges.pop(0)
    else:
        print("There are no available edges")
        return
        

    

def printNodesReached():
    print("-----Nodes Reached------")
    for i in range(0, len(nodesReached)):
        print(nodesReached[i].id)
    print("------------------------")

def printAvailableEdges():
    print("-----Available Edges------")
    for i in range(0, len(availableEdges)):
        print("- " + str(availableEdges[i].weight) + " -> " + str(availableEdges[i].otherNode.id))
    print("--------------------------")




graph = Graph(8)
graph.print()

prim(graph)

