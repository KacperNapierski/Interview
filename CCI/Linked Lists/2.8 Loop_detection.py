class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return str(nodes)
    
    def __iter__(self) -> None:
        node = self.head
        while node is not None:
            yield node
            node = node.next

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.visited = False

    def __repr__(self) -> str:
        return str(self.data)
    
llist = LinkedList()
node1 = Node('A')
llist.head = node1
node2 = Node('B')
node1.next = node2
node3 = Node('C')
node2.next = node3
node4 = Node('D')
node3.next = node4
node5 = Node('E')
node4.next = node5
node5.next = node3

#dictionary
def loop_detection_dict(llist):
    node = llist.head
    dict = {}
    while node is not None:
        if node in dict:
            dict[node] += 1
        else:
            dict[node] = 1

        if dict[node] == 2:
            break
        node = node.next
    return node.data

def loop_detection_pointers(llist):
    node1 = llist.head
    node2 = llist.head
    collision = False

    while node1 is not None:
        node1 = node1.next.next
        node2 = node2.next

        if node1 == node2:
            collision = True
            node2 = llist.head
        
        while collision == True:
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next


        


#print(loop_detection_dict(llist))
print(loop_detection_pointers(llist))