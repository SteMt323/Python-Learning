"""
Contar nodos
Escriba una función que cuente cuantos nodos tiene el arbol.
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
            
    def count_nodes(self):
        return self.aux_count_nodes(self.root)
    
    def aux_count_nodes(self, node) -> int:
        if node is None:
            return 0
        return 1 + self.aux_count_nodes(node.left) + self.aux_count_nodes(node.right)
    
    def print_nodes(self):
        if not self.root:
            print("Sin nodos...")
            return
        return self.aux_print_nodes(self.root)
    
    def aux_print_nodes(self, node):
        if node is not None:
            self.aux_print_nodes(node.left)
            print(node.data, end=" - ")
            self.aux_print_nodes(node.right)
        
    
def main():
    binary_tree: BinaryTree = BinaryTree()
    lista = [1, 3, 5, 2, 4, 6]
    for data in lista:
        binary_tree.insertion(data)
    binary_tree.print_nodes()
    print(f"\nNumero de nodos: {binary_tree.count_nodes()}")
    
if __name__ == "__main__":
    main()