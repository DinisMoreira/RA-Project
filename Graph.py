import random
from Edge import Edge
from Node import Node

class Graph:

    def __init__(self, nodesNum, seed, excludingEdges):
        self.nodes = []
        self.edges = []

        if(seed):
            print("Seed: " + str(seed))
            random.seed(seed)
        else:
            print("No Seed")
            random.seed()

        #Generate Nodes
        for i in range(0, nodesNum):
            newNode = Node(i)
            self.nodes.append(newNode)
        
        #Generate Node Edges
        maximumEdgeWeight = 1
        if(excludingEdges):
            maximumEdgeWeight = 1/(0.075 * nodesNum)
            print("Excluding every edge with weight above: " + str(maximumEdgeWeight))
        for i in range(0, nodesNum):
            for j in range(0, nodesNum):
                if(i < j):
                    weight = random.random()
                    if(weight < maximumEdgeWeight or not excludingEdges):
                        newEdge = Edge(self.nodes[i], self.nodes[j], weight)
                        self.nodes[i].connectedEdges.append(newEdge)               
        

    def print(self):
        for i in range(0, len(self.nodes)):
            print("Node " + str(self.nodes[i].id))
            for j in range(0, len(self.nodes[i].connectedEdges)):
                print("\tEdge to Node " + str(self.nodes[i].connectedEdges[j].otherNode.id) + " with weight: " + str(self.nodes[i].connectedEdges[j].weight))