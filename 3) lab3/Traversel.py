
class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root= new_node
            return
        
        currentNode = self.root
        while True:
            if data< currentNode.data:
                c
            
        