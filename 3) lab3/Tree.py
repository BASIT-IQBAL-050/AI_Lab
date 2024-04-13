from collections import deque
import queue


class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
    
    
    # Inserting an element.........................    
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return 
        
        current_node = self.root
        while True:
            if data<current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    return 
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return 
                current_node = current_node.right
                
    # Inserting after .....................
    def insert_After(self, data, after):
        if self.root is None:
            return False
        
        new_node = Node(data)
        current_node = self.root
        
        while current_node:
            if after == current_node.data:
                if data< current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return True
                    else:
                        sub_tree = current_node.left
                        current_node.left= new_node
                        if sub_tree.data < current_node.left.data:
                            current_node.left.left= sub_tree
                        else:
                            current_node.left.right = sub_tree
                        return True
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return True
                    else:
                        sub_tree = current_node.right
                        current_node.right= new_node
                        
                        if sub_tree.data < current_node.right.data:
                            current_node.right.left = sub_tree
                            
                        else:
                            current_node.right.right = sub_tree
                        return True
            elif after < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
    
    
                
    def Left_Order_Traversel(self,root):
        if root is not None:
            self.Left_Order_Traversel(root.left)
            print(root.data, end=" ")
            self.Left_Order_Traversel(root.right)
            return True
        return False
        
            
    def Right_Order_Traversel(self, root):
        if root:
            self.Right_Order_Traversel(root.right)
            print(root.data, end=" ")
            self.Right_Order_Traversel(root.left)
            return True
        return False
    
    def In_Order_Traversel(self, root):
        if root:
            print(root.data,  end=" ")
            self.In_Order_Traversel(root.left)
            self.In_Order_Traversel(root.right)
            return True
        return False
    
    def Level_Order_Traversel(self,root):
        if root is None:
            print("Tree is Empty")
            return 
        
        queue = deque()
        queue.append(root)
            
        while queue:
            node = queue.popleft()
            print(node.data, end=" ")
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    #Breadth First Search is similar to the Level_order_Traversel we just have to stop when we find the goal state
    def Breadth_First_Search(self, root, element):
        if root is None:
            return False
        
        queue= deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node.data == element:
                return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.right(node.right)
                

        return False
    
    # in depth first search we store the right node first so that it is poped at the last....................
    def Depth_First_Search(self,root, element):
        if root is None:
            return None
        
        stack = deque()
        stack.append(root)
        
        while stack:
            node = stack.pop()
            
            if node.data == element:
                return True
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return False
                
tree = Tree()
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(5)
tree.insert(7)


# data = int(input("Enter the number you want to add : "))
# before = int(input("Enter the number before  which you want to add : "))
# tree.insert_After(data, before)
# print("tree.root is ", tree.root)
# tree.In_Order_Traversel(tree.root)
tree.Left_Order_Traversel(tree.root)
