class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right
                
    def find(self, data):
        if self.root is None:
            return False
        current_node = self.root
        while current_node:
            if current_node.data == data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def insertAfter(self, data, after):
        if self.root is None:
            return False

        new_node = Node(data)
        current_node = self.root

        while current_node:
            if after == current_node.data:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return True
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return True
                    current_node = current_node.right
            elif after < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return False

tree = Tree()
tree.insert('L')
tree.insert('E')    
tree.insert('D')
tree.insert('M')

character = input("Enter the element you want to add: ")
after = input("Enter the element after which you want to add: ")

if tree.insertAfter(character, after):
    print("Element added successfully")
else:
    print("Element could not be added.")
