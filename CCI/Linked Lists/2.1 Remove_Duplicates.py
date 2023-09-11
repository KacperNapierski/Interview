class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self):
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
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
    
    def __repr__(self) -> str:
        return self.data



##example program input
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


### dictionary + dunder
def remove_duplicates_dict(llist:LinkedList):
    hashset = set()
    print(llist)

    if llist.head is None:
        raise Exception("THERE IS NO LIST")
    
    previous_node = llist.head
    for node in llist:
        if node.data in hashset:
            previous_node.next = node.next
        else:
            hashset.add(node.data)
            previous_node = node

    return llist

### 2 pointers + manual
def remove_duplicates(llist:LinkedList):
    node_p1 = llist.head
    node_p2 = llist.head

    try:
        while node_p1.next is not None:
            node_p2 = node_p1
            while node_p2.next is not None:
                if node_p2.next.data == node_p1.data:
                    node_p2.next = node_p2.next.next
                node_p2 = node_p2.next
            node_p1 = node_p1.next
    except:
        print("finished looping")
    return llist
    

if __name__ == "__main__":
    print(remove_duplicates_dict(llist))
    print('#############')
    print(remove_duplicates(llist))