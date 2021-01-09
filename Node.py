class Node:

    def __init__(self, id):
        self.id = id
        self.connectedEdges = []

    def generateNewNodeEdge(self, weight):
        return
        
    def print(self):
        print("Node " + str(self.id))
        return