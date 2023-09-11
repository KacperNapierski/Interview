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
    
    #def remove_node(self, target) -> None:
    #    if self.head is None:
    #        raise Exception("THERE IS NO LIST")
    #    elif self.head == target:
    #        self.head == self.head.next
    #        return
    #    
    #    previous_node = self.head
    #    for node in self:
    #        if node.data == target:
    #            previous_node.next = node.next
    #            return
    #        
    #    raise Exception(f"NO {target} IN THE LIST")
    

class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
    
    def __repr__(self) -> str:
        return self.data



##exampl program input
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



def remove_duplicates(llist:LinkedList):
    hashset = set()
    print(llist)

    if llist.head is None:
        raise Exception("THERE IS NO LIST")
    
    #hashset.add(llist.head)
    previous_node = llist.head
    for node in llist:
        if node.data in hashset:
            previous_node.next = node.next
        else:
            hashset.add(node.data)
            previous_node = node
        print(llist)
        print(hashset)
        print('###')


    #node = llist.head    

if __name__ == "__main__":
    remove_duplicates(llist)