"""
Estructura basica de un arbol binario.
Funciones:
- Insersion
- Eliminacion
- Busqueda
- Impresión
"""
# Todo funciona con la recursividad aqui alv

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
        if self.root is None:
            self.root = new_node
            return
        self.insertion_aux(self.root, new_node)
        
    def insertion_aux(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self.insertion_aux(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.insertion_aux(current.right, new_node)
                
    def delete_node(self, data):
        self.root = self.aux_delete_node(self.root, data)
        
    def aux_delete_node(self, current, data):
        if not current:
            print("Arbol vacio")
            return
        
        if data < current.data:
            current.left = self.aux_delete_node(current.left, data)
        elif data > current.data:
            current.right = self.aux_delete_node(current.right, data)
        else:
            # Caso 1: Nodo Hoja
            if not current.left and not current.right:
                return None
            # Caso 2: 1 Nodo Hijo 
            elif not current.right:
                return current.left
            elif not current.left:
                return current.right
            # Caso 3: 2 Nodos Hijos
            else:
                sucesor = self.search_sucesor_node(current.right)
                current.data = sucesor.data
                current.right = self.aux_delete_node(current.right, sucesor.data)
        return current
      
    def search_sucesor_node(self, node) -> any:
        current = node
        while current.left:
            current = current.left
        return current
    
    def search_node(self, data):
        return self.aux_search_node(self.root, data)
    
    def aux_search_node(self, node, data):
        if not node:
            return None
        if data == node.data:
            return node.data
        elif data < node.data:
            return self.aux_search_node(node.left, data)
        elif data > node.data:
            return self.aux_search_node(node.right, data)
    
    def print_inorder(self):
        self.aux_print_inorder(self.root)
        
    def aux_print_inorder(self, node):
        if node is not None:
            self.aux_print_inorder(node.left)
            print(node.data)
            self.aux_print_inorder(node.right)
            
def main():
    binary_tree: BinaryTree = BinaryTree()
    binary_tree.insertion(2)
    binary_tree.insertion(7)
    binary_tree.insertion(2)
    binary_tree.insertion(4)
    binary_tree.insertion(3)
    binary_tree.insertion(1)
    print("Datos ordenados del arbol binario: ")
    binary_tree.print_inorder()
    binary_tree.delete_node(4)
    print("Arbol sin el valor 4")
    binary_tree.print_inorder()    
    print("Buscar el nodo con valor 7")
    print(binary_tree.search_node(7))
    
if __name__ == "__main__":
    main()