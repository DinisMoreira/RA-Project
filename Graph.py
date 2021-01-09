import random
from Edge import Edge
from Node import Node

class Graph:

    def __init__(self, nodesNum):
        self.nodes = []
        self.edges = []

        for i in range(0, nodesNum):
            newNode = Node(i)
            self.nodes.append(newNode)

        #Generate Node Edges
        for i in range(0, nodesNum):
            for j in range(0, nodesNum):
                if(i < j):
                    newEdge = Edge(self.nodes[j],random.uniform(0, 1))
                    self.nodes[i].connectedEdges.append(newEdge)
                #elif(i > j):
            
            #generate new random weight for edges connected to nodes with bigger id numbers
            #get the weight of the existing edge from the edges connected to nodes with lower id numbers


    def print(self):
        #print("Nodes = " + str(self.nodes))
        #print("Edges = " + str(self.edges))
        return