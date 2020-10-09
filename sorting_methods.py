import tree


def tree_sort(array):
    """
    Tree sort is based on Binary Search Tree data structure.
    It creates a binary tree from the elements of the array
    and then adds elements to new, sorted array going in-order throught the tree
    """
    if len(array) == 0:
        return array

    root = tree.Node(array[0])
    for i in range(1, len(array)):
        root.insert(array[i])

    sorted_array = []
    tree.inorder(root, sorted_array)
    return sorted_array


if __name__ == "__main__":
    unsorted_numbers = [-7.23, 19, 3.256, 9909, 0.000002, -45.23, -0.0002, 19, 0.0]
    print("Array to sort:\t", unsorted_numbers)

    tree_sorted_array = tree_sort(unsorted_numbers)
    print("Tree sort:\t", tree_sorted_array)
