class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None 
        self.parent = None 
        self.height = 0 # need height to calculate the balance factor (bf) 

class AVL:
    def __init__(self):
        self.root = None 

    def get_height(self, node):
        if node is None:
            return -1 # cannot use None 
        return node.height
    
    def get_balance_factor(self, node):
        if node is None:
            return 0 
        return self.get_height(node.left) - self.get_height(node.right) # subtraction of the height of the subtree

    def update_height(self,node): # internal update  on the height of a node, get the higher height
        if node is not None:
            if self.get_height(node.left) > self.get_height(node.right):
                node.height = 1 + self.get_height(node.left)
            else:
                node.height = 1 + self.get_height(node.right)

    ######################
    # 1. Single right rotation, leaning on the right
    def single_right_rotation(self, pivot_node):
        stay_node = pivot_node.left # leaning on the right, thus its stay node is on the left

        # Part 1: Since the pivot node will go down as a right child of the stay node,
        # Connect the the right child of the stay node as the left child of the pivot node
        pivot_node.left = stay_node.right # let the new left child of pivot node be the current right of the stay node (if there is any)
        if stay_node.right is not None:
            stay_node.right.parent = pivot_node  # connect and update the new parent of the child

        stay_node.right = pivot_node # move down the pivot node as the right of the stay node

        stay_node.parent = pivot_node.parent # update the new parent of the stay node, connect it to the parent of the pivot node

        if pivot_node.parent is None: # Just in case the pivot node has no parent, it means it is the root node
            self.root = stay_node
        elif pivot_node == pivot_node.parent.left: # check if pivot node is a left child
            pivot_node.parent.left = stay_node # update the new child of the pivot's parent to be the stay node
        else: # if the pivot node is a right child
            pivot_node.parent.right = stay_node

        pivot_node.parent = stay_node # Finally update the new parent of the pivot node

        self.update_height(pivot_node)
        self.update_height(stay_node)
        
        # Display tree after rotation
        print(f"\n  >>> After Single Right Rotation at node {pivot_node.info}:")
        self.display_tree(self.root)
        return stay_node

    def single_left_rotation(self, pivot_node):
        stay_node = pivot_node.right
        # child of pivot node
        pivot_node.right = stay_node.left
        if stay_node.left is not None:
            stay_node.left.parent = pivot_node

        stay_node.left = pivot_node

        stay_node.parent = pivot_node.parent 
        if pivot_node.parent is None:
            self.root = stay_node
        elif pivot_node.parent.left == pivot_node:
            pivot_node.parent.left = stay_node
        else:
            pivot_node.parent.right = stay_node      

        pivot_node.parent = stay_node

        self.update_height(pivot_node)
        self.update_height(stay_node)
        
        # Display tree after rotation
        print(f"\n  >>> After Single Left Rotation at node {pivot_node.info}:")
        self.display_tree(self.root)
        return stay_node

    def double_right_rotation(self, pivot_node): # left-right rotation
        print(f"\n  >>> Performing Double Right Rotation at node {pivot_node.info}:")
        print("      Step 1: Single Left Rotation on left child")
        pivot_node.left = self.single_left_rotation(pivot_node.left)
        print("      Step 2: Single Right Rotation on pivot node")
        return self.single_right_rotation(pivot_node)
    
    def double_left_rotation(self, pivot_node): # right-left rotation 
        print(f"\n  >>> Performing Double Left Rotation at node {pivot_node.info}:")
        print("      Step 1: Single Right Rotation on right child")
        pivot_node.right = self.single_right_rotation(pivot_node.right)
        print("      Step 2: Single Left Rotation on pivot node")
        return self.single_left_rotation(pivot_node)
    
    def balance_tree(self, node):
        balance_factor = self.get_balance_factor(node)

        print("\nTree BEFORE rotation:")
        self.display_tree(self.root)

        if balance_factor == 2:
            if self.get_balance_factor(node.left) >= 0 : # leaning to the right
                print(f"\n  >>> Balance Factor {balance_factor}: Single Right Rotate at node {node.info}")
                result = self.single_right_rotation(node)
            else: # the bf of node.left is -1 thus a right-left rotation
                print(f"\n  >>> Balance Factor {balance_factor}: Double Right Rotate at node {node.info}")
                result = self.double_right_rotation(node)

        elif balance_factor == -2:
            if self.get_balance_factor(node.right) <= 0:
                print(f"\n  >>> Balance Factor {balance_factor}: Single Left Rotate at node {node.info}")
                result = self.single_left_rotation(node)
            else: 
                print(f"\n  >>> Balance Factor {balance_factor}: Double Left Rotate at node {node.info}")
                result = self.double_left_rotation(node)

        print("\nTree AFTER rotation:")
        self.display_tree(self.root)

        return result
    
    def insert(self, info):
        print(f"\n{'='*50}")
        print(f"Inserting node with value: {info}")
        print('='*50)
        
        new_node = Node(info)

        trailing_node = None
        current_node = self.root 

        while current_node is not None:
            trailing_node = current_node
            if info < current_node.info:
                current_node = current_node.left 
            else:
                current_node = current_node.right 

        new_node.parent = trailing_node

        if trailing_node is None:
            self.root = new_node
        else:
            if info < trailing_node.info:
                trailing_node.left = new_node
            else:
                trailing_node.right = new_node
        

        print(f"\nInserted {info}")
        # self.display_tree(self.root)
        # self.update_heights_upwards(new_node)
        # Display tree after insertion (before balancing)
        # print(f"\n>>> Tree after inserting {info} (before balancing):")
        # self.display_tree(self.root)
        
        # Every time insertion happens, the height of every ancestor node changes. Thus the reason
        # for traversal. It is bottoms up because the imbalance always happens closest to the new node
        pointer = new_node
        
        while pointer is not None:
            self.update_height(pointer)
            balance_factor = self.get_balance_factor(pointer)

            if abs(balance_factor) == 2:
                # print(f"\n>>> Imbalance detected at node {pointer.info} (BF = {balance_factor})")
                self.balance_tree(pointer)
                break 

            pointer = pointer.parent
            
        self.display_tree(self.root)
        # If no rotation was performed, show the final tree
        # if not rotation_performed:
        #     print(f"\n>>> Final tree after inserting {info} (no rotation needed):")
        #     self.display_tree(self.root)
        # else:
        #     print(f"\n>>> Final tree after inserting {info} (rotation completed):")
        #     self.display_tree(self.root)

    def display_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.info) + f" (bf:{self.get_balance_factor(node)})")
            if node.left is not None or node.right is not None:
                if node.left:
                    self.display_tree(node.left, level + 1, prefix="L── ")
                else:
                    print(" " * ((level + 1) * 4) + "L── None")
                if node.right:
                    self.display_tree(node.right, level + 1, prefix="R── ")
                else:
                    print(" " * ((level + 1) * 4) + "R── None")

