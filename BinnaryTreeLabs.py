class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def inorder_traversal(root, array):
    if root is not None:
        inorder_traversal(root.left, array)
        array.append(root.value)
        inorder_traversal(root.right, array)
    return array

def successor(root, our_elem):
    empty_arr = []
    sorted_array = inorder_traversal(root, empty_arr)
    print(sorted_array)
    index = sorted_array.index(our_elem.value)
    for i in range(1, len(sorted_array)):
        if index + i > len(sorted_array) - 1:
            return False
        elif sorted_array[index + i] > sorted_array[index]:
            return sorted_array[index + i]

