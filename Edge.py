class Edge:

    def __init__(self, otherNode, weight):
        self.otherNode = otherNode
        self.weight = weight

    def print(self):
        print("Connection to node " + str(self.otherNode) + " = " + str(self.weight))
        return