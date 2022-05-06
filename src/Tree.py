
class Node:
    def __init__(self, position, cost=0, depth=0, parent=None):
        self.position = position
        self.cost = cost
        self.adj = []
        self.parent = parent
        self.depth = depth

    def getPriority(self):
        return self.cost


class Tree:
    def __init__(self, position, isCost=True):
        if(isCost):
            self.root = Node(position, 0)
        else:
            self.root = Node(position)
