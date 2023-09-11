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
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data
    

llist = LinkedList()
node1 = Node(1)
llist.head = node1
node2 = Node(3)
node1.next = node2
node3 = Node(4)
node2.next = node3
node4 = Node(3)
node3.next = node4
node5 = Node(2)
node4.next = node5
node6 = Node(1)
node5.next = node6
node7 = Node(5)
node6.next = node7
node8 = Node(5)
node7.next = node8

k = 3

##dunder
def kth_2_last_element_dunder(llist,k):
    count = 0
    for node in llist:
        count += 1
    for node in llist:
        if count == k:
            return node.data
        count -= 1


##manual
def kth_2_last_element(llist,k):
    count = 0
    node = llist.head
    while node is not None:
        count +=1
        node = node.next

    node = llist.head
    while node is not None:
        if count == k:
            return node.data
        count -= 1
        node = node.next

##2 pointers
def kth_element_pointers(llist,k):
    node_p1 = llist.head
    node_p2 = llist.head

    for _ in range(k):
        if node_p2.data == None: return 0
        node_p2 = node_p2.next

    while node_p2 is not None:
        node_p2 = node_p2.next
        node_p1 = node_p1.next

    return node_p1.data

if __name__ == '__main__':
    print(kth_2_last_element_dunder(llist,k))
    print(kth_2_last_element(llist,k))
    print(kth_element_pointers(llist,k))