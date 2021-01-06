import random

class Edge:

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.weight = random.uniform(0, 1)

    def print(self):
        print("Node 1 = " + str(self.node1))
        print("Node 2 = " + str(self.node2))
        print("Weight = " + str(self.weight))
        return