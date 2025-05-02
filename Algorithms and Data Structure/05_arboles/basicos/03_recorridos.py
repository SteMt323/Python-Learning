"""
Recorridos en orden, preorden y postorden
Implemente los tres recorridos y hacé que impriman los valores.
"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None 
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insertion(self, data):
        new_node: Node = Node(data)
        if not self.root:
            self.root = new_node
            return
        self.aux_insertion(self.root, new_node)
        
    def aux_insertion(self, current, new_node):
        if new_node.data < current.data:
            if not current.left:
                current.left = new_node
            else: self.aux_insertion(current.left, new_node)
        else:
            if not current.right:
                current.right = new_node
            else: self.aux_insertion(current.right, new_node)
       
    # In Order     
    def print_inorder(self):
        return self.aux_print_inorder(self.root)
    
    def aux_print_inorder(self, node):
        if node is not None:
            self.aux_print_inorder(node.left)
            print(node.data)
            self.aux_print_inorder(node.right)
    
    # Pre Order        
    def print_preorder(self):
        return self.aux_print_preorder(self.root)
    
    def aux_print_preorder(self, node):
        if node is not None:
            print(node.data)
            self.aux_print_preorder(node.left)
            self.aux_print_preorder(node.right)
            
    # Post Order
    def print_postorder(self):
        return self.aux_print_postorder(self.root)
    
    def aux_print_postorder(self, node):
        if node is not None:
            self.aux_print_postorder(node.left)
            self.aux_print_postorder(node.right)
            print(node.data)
            
def main():
    binary_tree: BinaryTree = BinaryTree()
    lista = [1, 3, 5, 2, 4, 6]
    for data in lista:
        binary_tree.insertion(data)
    print("In Order: ")    
    binary_tree.print_inorder()
    print("\nPre Order:")
    binary_tree.print_preorder()
    print("\nPost Order: ")
    binary_tree.print_postorder()
    
if __name__ == "__main__":
    main()