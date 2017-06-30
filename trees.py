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