import random

class Graph:

    def __init__(self, nodesNum):
        self.nodes = []
        self.edges = []

        for i in range(0, nodesNum):
            self.nodes.append(i)

    def print(self):
        print("Nodes = " + str(self.nodes))
        print("Edges = " + str(self.edges))
        return