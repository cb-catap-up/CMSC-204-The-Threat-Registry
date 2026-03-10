import time
class Node:
    def __init__(self, info):
        self.info = info
        self.right = None 
        self.left = None 
        self.parent = None 
        self.height = 0 # need height to calculate the balance factor (bf) 

    
class BST:
    def __init__(self):
        self.root = None 

    def insert(self, info):
        new_node = Node(info)

        # goal is to traverse and go to the left most or right most node 
        # but you need to get the information of the parent node or trailing node
        trailing_node = None 
        current_node = self.root

        while current_node is not None:
            trailing_node = current_node
            if info < current_node.info:                
                current_node = current_node.left
            else:
                current_node = current_node.right
                

        if trailing_node is None:
            self.root = new_node
            print(f'\nInserting {info}')
            #time.sleep(1)
            self.display_tree(self.root)

        else:
            new_node.parent = trailing_node # use trailing_node instead of current_node, current_node needs to be none inorder to break the loop   
            if info < trailing_node.info:
                trailing_node.left = new_node
                print(f'\nInserting {info}')
                #time.sleep(1)
                self.display_tree(self.root)
            else:
                trailing_node.right = new_node
                print(f'\nInserting {info}')
                #time.sleep(1)
                self.display_tree(self.root)

    def display_preorder(self, tree):
        if tree is None:
            return
        print(tree.info, end=' ')
        self.display_preorder(tree.left)
        self.display_preorder(tree.right) 
    
    def display_postorder(self, tree):
        if tree is None:
            return
        self.display_postorder(tree.left)
        self.display_postorder(tree.right)
        print(tree.info, end=' ') 


    def display_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.info) )
            if node.left is not None or node.right is not None:
                if node.left:
                    self.display_tree(node.left, level + 1, prefix="L── ")
                else:
                    print(" " * ((level + 1) * 4) + "L── None")
                if node.right:
                    self.display_tree(node.right, level + 1, prefix="R── ")
                else:
                    print(" " * ((level + 1) * 4) + "R── None")

