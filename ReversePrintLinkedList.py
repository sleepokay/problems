def ReversePrint(node):
    if not node:
        return
           
    if node:
        ReversePrint(node.next)
        print(node.data)