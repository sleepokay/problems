
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


# check two linked lists for equality
def CompareLists(nodeA, nodeB):
    while nodeA or nodeB:
        if nodeA and nodeB and nodeA.data == nodeB.data:
            nodeA = nodeA.next
            nodeB = nodeB.next
        else: 
            return 0    
    return 1


# merge two sorted linked lists in ascending order
def MergeLists(nodeA, nodeB): 
    new_head = None
    if nodeA and nodeB:
        if nodeA.data < nodeB.data:
            new_head = nodeA
            nodeA = nodeA.next
        else:
            new_head = nodeB
            nodeB = nodeB.next
    elif not nodeA:
        return nodeB
    elif not nodeB:
        return nodeA
    
    current = new_head
    
    while nodeA or nodeB:       
        if not nodeA:
            current.next = nodeB
            return new_head
        elif not nodeB:
            current.next = nodeA
            return new_head
        elif nodeA.data < nodeB.data:
            current.next = nodeA
            nodeA = nodeA.next
            current = current.next
        elif nodeA.data >= nodeB.data:
            current.next = nodeB
            nodeB = nodeB.next
            current = current.next
            
    return new_head

# Floyd's algorithm for cycle detection
def has_cycle(node):
    if not node:
        return 0
    
    turtle = node
    hare = node
    
    while not hare is None and not hare.next is None:
        turtle = turtle.next
        hare = hare.next.next
        
        if turtle is hare:
            return 1
    return 0
