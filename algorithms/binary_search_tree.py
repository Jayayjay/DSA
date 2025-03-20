class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value) #Insert as left
            else:
                self._insert_recursive(node.left, value)
                
    
    def delete(self, value):
        pass

    def search(self, value):
        pass
    
    def get_min(self):
        pass
    
    def get_max(self):
        pass
    
    # Traversal methods
    
    def in_order_traversal():
        pass
    
    def pre_order_traversal():
        pass
    
    def post_order_traversal():
        pass
    