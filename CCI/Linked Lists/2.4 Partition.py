    
class Node:
    def __init__(self,data) -> None:
        self.next = None
        self.data = data
    
    def __repr__(self) -> str:
        return self.data
    

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
    
    def add_first(self, node:Node):
        node.next = self.head
        self.head = node 



llist = LinkedList()
node1 = Node(3)
llist.head = node1
node2 = Node(5)
node1.next = node2
node3 = Node(8)
node2.next = node3
node4 = Node(5)
node3.next = node4
node5 = Node(10)
node4.next = node5
node6 = Node(2)
node5.next = node6
node7 = Node(1)
node6.next = node7

breaking_point = 5

## 2 lists
def partition(llist, breaking_point):
    node = llist.head
    #dummy nodes
    left, right = LinkedList(), LinkedList()
    l_node, r_node = Node(0), Node(0)
    left.head = l_node
    right.head = r_node

    #segragating to lists
    while node is not None:
        if node.data < breaking_point:
            l_node.next = Node(node.data)
            l_node = l_node.next
        else:
            r_node.next = Node(node.data)
            r_node = r_node.next
        node = node.next

    #connecting lists + clearing left dummy node
    l_node.next= right.head.next
    left.head = left.head.next
    r_node.next = None

    return left


if __name__ == "__main__":
    print(partition(llist, breaking_point))