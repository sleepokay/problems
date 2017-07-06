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


# print level order
import Queue
def levelOrder(root):
    if not root:
        return
    
    q = Queue.Queue()
    q.put(root)
    
    while not q.empty():
        node = q.get()
        sys.stdout.write(str(node.data) + ' ')
        
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
       
    