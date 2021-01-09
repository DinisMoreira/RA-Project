from functools import total_ordering 

@total_ordering
class Edge:

    def __init__(self, otherNode, weight):
        self.otherNode = otherNode
        self.weight = weight

    def __lt__(self, other): 
        return self.weight < other.weight 