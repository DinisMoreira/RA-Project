import random
import bisect
import time
import string
from operator import attrgetter
from Graph import Graph
from Edge import Edge

selectedEdges = []
nodesReached = []
availableEdges = []


def prim(graph, removingEdges):
    graphSize = len(graph.nodes)


    print("PRIM'S ALGORITHM : " + str(graphSize))
    startTime = time.time()

    if(removingEdges):
        removeBigEdges(graph, graphSize)

    currentVertexIndex = 0#random.randint(0, graphSize-1)#RANDOM
    #print("Initial Vertex = " + str(currentVertexIndex))

    currentNode = graph.nodes[currentVertexIndex]

    while(len(nodesReached) < graphSize):

        newNodeReached(graph, currentNode)
        
        #printNodesReached()
        #printAvailableEdges()

        if(len(availableEdges) > 0):
            bestAvailableEdge = getBestAvailableEdge()
            selectedEdges.append(bestAvailableEdge)
            #print("Lowest available edge: " + str(bestAvailableEdge.weight) + " to node " + str(bestAvailableEdge.otherNode.id))
            currentNode = bestAvailableEdge.otherNode
        
        #print(str(len(nodesReached)) + "/" + str(graphSize))
        
    endTime = time.time()
    if(graphSize <= 64):
        printSelectedEdges()
    print("Elapsed Time: " + str(endTime-startTime) + " s")
    print("Sum of all edges weight in MST: " + str(sum(edge.weight for edge in selectedEdges)))
    print("Weight of the edge with the biggest weight in the MST: " + str(max(selectedEdges).weight))
    
    

def newNodeReached(graph, newNode):
    #Remove every edge on other nodes that connects to the reached node in either originalNode or otherNode
    #Add the new edges from the new node to the "availabreEdges" vector, if needed altered with the newNode in the originalNode
    for node in graph.nodes:
        for edge in reversed(graph.nodes[node.id].connectedEdges):
            #print("Checking edge: " + str(edge.originalNode.id) + " -> " + str(edge.otherNode.id))
            if(edge.originalNode.id == newNode.id):
                #print("Insert into availableEdges the original edge: " + str(edge.originalNode.id) + " -> " + str(edge.otherNode.id))
                bisect.insort(availableEdges, edge)
                graph.nodes[node.id].connectedEdges.remove(edge)
            elif(edge.otherNode.id == newNode.id):
                reversedEdge = Edge(edge.otherNode, edge.originalNode, edge.weight)
                #print("Insert into availableEdges the reversed edge: " + str(reversedEdge.originalNode.id) + " -> " + str(reversedEdge.otherNode.id))
                bisect.insort(availableEdges, reversedEdge)
                graph.nodes[node.id].connectedEdges.remove(edge)

    

    """print("-----------------UPDATED GRAPH-----------------")
    for node in graph.nodes:
        for edge in graph.nodes[node.id].connectedEdges:
            print("Node " + str(edge.originalNode.id) + ", edge " + str(edge.otherNode.id))
    print("-----------------------------------------------")"""

    #Remove every edge on "availableEdges" that leads to the reached node
    availableEdges[:] = [edge for edge in availableEdges if not (edge.otherNode.id == newNode.id)]

    #Add new node to "nodesReached" vector
    nodesReached.append(newNode)


def removeBigEdges(graph, graphSize):
    maximumEdgeWeight = 0.4-0.000048*graphSize
    print("Biggest edge: " + str(maximumEdgeWeight))
    i=0
    for node in graph.nodes:
        print(i)
        i = i + 1
        for edge in reversed(graph.nodes[node.id].connectedEdges):
            if(edge.weight > maximumEdgeWeight):
                graph.nodes[node.id].connectedEdges.remove(edge)
                #print("Removing edge " + str(edge.originalNode.id) + " - " + str(edge.weight) + " -> " + str(edge.otherNode.id))


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
        print(str(availableEdges[i].originalNode.id) + " - " + str(availableEdges[i].weight) + " -> " + str(availableEdges[i].otherNode.id))
    print("--------------------------")

def printSelectedEdges():
    print("-----------Selected Edges-----------")
    for i in range(0, len(selectedEdges)):
        print(str(selectedEdges[i].originalNode.id) + " - " + str(selectedEdges[i].weight) + " -> " + str(selectedEdges[i].otherNode.id))
    print("------------------------------------")


numberOfNodes = 16
removingEdges = True
seed = None
graph = Graph(numberOfNodes, seed)
#graph.print()
prim(graph, removingEdges)