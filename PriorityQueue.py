

class PriorityQueue:
    # a constructor that takes a boolean value (true for descending).
    def __init__(self, descending=False):
        self.elements = list()
        self.size = 0
        self.descending = descending

    # a function that returns (true: if empty false otherwise).
    def is_empty(self):
        return len(self.elements) == 0

    # a function that inserts a node in the queue based on it's priority.
    def enqueue(self, node):
        if(self.size == 0):
            self.elements.append(node)
        elif(self.descending):
            for x in range(self.size):
                if(node.getPriority() > self.elements[x].getPriority()):
                    self.elements.insert(x, node)
                    self.size += 1 
                    return
            self.elements.append(node)
        else:
            for x in range(self.size):
                if(node.getPriority() < self.elements[x].getPriority()):
                    self.elements.insert(x, node)
                    self.size += 1 
                    return
            self.elements.append(node)
        self.size += 1 

    # returning the first element and remove it from the queue.
    def pop(self):
        if not self.is_empty():
            temp = self.elements.pop(0)
            self.size -= 1
            return temp
        else:
            return None

