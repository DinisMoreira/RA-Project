import random
from Edge import Edge
from Node import Node

class Graph:

    def __init__(self, nodesNum):
        self.nodes = []
        self.edges = []

        #Generate Nodes
        for i in range(0, nodesNum):
            newNode = Node(i)
            self.nodes.append(newNode)

        #Generate Node Edges
        for i in range(0, nodesNum):
            for j in range(0, nodesNum):
                if(i < j):
                    newEdge = Edge(self.nodes[j],random.uniform(0, 1))#RANDOM
                    self.nodes[i].connectedEdges.append(newEdge)
                elif(i > j):
                    newEdge = Edge(self.nodes[j], self.nodes[j].connectedEdges[i-1].weight) 
                    self.nodes[i].connectedEdges.append(newEdge)
                
        

    def print(self):
        for i in range(0, len(self.nodes)):
            print("Node " + str(self.nodes[i].id))
            for j in range(0, len(self.nodes[i].connectedEdges)):
                print("\tEdge to Node " + str(self.nodes[i].connectedEdges[j].otherNode.id) + " with weight: " + str(self.nodes[i].connectedEdges[j].weight))