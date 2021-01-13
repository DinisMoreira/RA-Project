import random
from Edge import Edge
from Node import Node

class Graph:

    def __init__(self, nodesNum, seed):
        self.nodes = []
        self.edges = []

        if(seed):
            print("Seed: " + str(seed))
            random.seed(seed)
        else:
            print("No Seed")
            random.seed()
        #Initiate seed with a value to repeatedly generate the same random weighted edges
        #if left empty the current system time is used

        #Generate Nodes
        for i in range(0, nodesNum):
            newNode = Node(i)
            self.nodes.append(newNode)

        #Generate Node Edges
        for i in range(0, nodesNum):
            for j in range(0, nodesNum):
                if(i < j):
                    newEdge = Edge(self.nodes[i], self.nodes[j],random.random())#RANDOM
                    self.nodes[i].connectedEdges.append(newEdge)               
        

    def print(self):
        for i in range(0, len(self.nodes)):
            print("Node " + str(self.nodes[i].id))
            for j in range(0, len(self.nodes[i].connectedEdges)):
                print("\tEdge to Node " + str(self.nodes[i].connectedEdges[j].otherNode.id) + " with weight: " + str(self.nodes[i].connectedEdges[j].weight))