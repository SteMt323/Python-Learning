"""
Insertar valores en el árbol desde una lista
Escribí una función que reciba una lista de números y los inserte todos en el árbol.
"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None 
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        new_node: Node = Node(data)
        if not self.root:
            self.root = new_node
            return
        self.aux_insertions(self.root, new_node)
    
    def aux_insertions(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else: self.aux_insertions(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else: self.aux_insertions(current.right, new_node)
            
    def insertion_list(self, list):
        for i, data in enumerate(list):
            self.insert(data)
            
    def print_inorder(self):
        return self.aux_print_inorder(self.root)
            
    def aux_print_inorder(self, node):
        if node is not None:
            self.aux_print_inorder(node.left)
            print(node.data)
            self.aux_print_inorder(node.right)
            
def main():
    binary_tree: BinaryTree = BinaryTree()
    lista = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]
    binary_tree.insertion_list(lista)
    binary_tree.print_inorder()
    
if __name__ == "__main__":
    main()