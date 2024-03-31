
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
                if currentNode.left is None:
                    currentNode.left=new_node
                    return
                currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right=new_node
                    return
                currentNode = currentNode.right

    def Left_Order_Traversal(self, root=None):
        if root:
            self.Left_Order_Traversal(root.left)
            print(root.data)
            self.Left_Order_Traversal(root.right)
    
    def Right_Order_Traversal(self, root=None):
        if root:
            self.Right_Order_Traversal(root.right)
            print(root.data)
            self.Right_Order_Traversal(root.left)
    
    def InOrder_Traversal(self, root=None):
        if root:
            print(root.data)
            self.InOrder_Traversal(root.left)
            self.InOrder_Traversal(root.right)
            

tree = Tree()
tree.insert('L')
tree.insert('E')    
tree.insert('D')
tree.insert('M')
tree.Left_Order_Traversal(tree.root)   
print("------------------------")   
tree.Right_Order_Traversal(tree.root)  
print("------------------------") 
tree.InOrder_Traversal(tree.root)   
            
        