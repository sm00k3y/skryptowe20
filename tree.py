class Node:

    def __init__(self, root_value):
        self.val = root_value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)


def inorder(root_node, sorted_array):
    if root_node:
        inorder(root_node.left, sorted_array)
        sorted_array.append(root_node.val)
        inorder(root_node.right, sorted_array)
