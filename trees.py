import sys

def preOrder(root):
    if not root:
        return
    
    sys.stdout.write(str(root.data) + " ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if not root:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    
    sys.stdout.write(str(root.data) + " ")


def inOrder(root):
    if not root:
        return
    
    inOrder(root.left)
    sys.stdout.write(str(root.data) + " ")
    inOrder(root.right)

# find height of binary tree
def height(node):
    if not node:
        return -1
    
    left_height = 1 + height(node.left)
    right_height = 1 + height(node.right)
    
    return max(left_height, right_height)
    