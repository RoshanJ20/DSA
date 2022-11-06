class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here
    if root == None:
        root = BinaryTreeNode(new_value)
    elif new_value < root.data:
        root.left = insert(root.left,new_value)
    else:
        root.right = insert(root.right,new_value)
    return root


def inorder(root) -> None:
    # Write your code here
    if root:
        inorder(root.left)
        print(root.data, end =' ')
        inorder(root.right)


def preorder(root) -> None:
    # Write your code here
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)


def postorder(root) -> None:
    # Write your code here
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = ' ')

# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
