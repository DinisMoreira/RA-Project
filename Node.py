class Node:

    def __init__(self, id):
        self.id = id
        self.connectedEdges = []
        
    def print(self):
        print("Node " + str(self.id))
        return