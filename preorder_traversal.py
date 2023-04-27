# Python3 program for tree traversals

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A function to do preorder tree traversal
def preorderTraversal(root):
    if root:
        # First print the data of node
        print(root.val, end=' ')
        # Then recur on left child
        preorderTraversal(root.left)
        # Finally recur on right child
        preorderTraversal(root.right)

# Driver code
if __name__ == "__main__":
    # Prompt user for input and convert to list of integers
    values = list(map(int, input("Enter the values for the binary tree separated by spaces: ").split()))

    # Create binary tree
    root = Node(values[0])
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if i < len(values):
            node.left = Node(values[i])
            queue.append(node.left)
            i += 1
        if i < len(values):
            node.right = Node(values[i])
            queue.append(node.right)
            i += 1

    # Function call
    print("Preorder traversal of binary tree is:")
    preorderTraversal(root)
