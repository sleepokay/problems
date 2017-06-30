
# print a linked list in reverse
def ReversePrint(node):
    if not node:
        return
           
    if node:
        ReversePrint(node.next)
        print(node.data)

# reverse a linked list
def Reverse(head):
    return ReverseHelp(head, None)
    
def ReverseHelp(node, prev):
    if not node:
        return prev

    temp = node.next
    node.next = prev
    return ReverseHelp(temp, node)