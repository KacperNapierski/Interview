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
    
    
class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
    
    def __repr__(self) -> str:
        return self.data
    

llist = LinkedList()
node1 = Node("a")
llist.head = node1
node2 = Node("b")
node1.next = node2
node3 = Node("c")
node2.next = node3
node4 = Node("d")
node3.next = node4
node5 = Node("e")
node4.next = node5
node6 = Node("f")
node5.next = node6

target_node = node3

def delete_middle(target_node):
    if target_node == None or target_node.next == None: return False

    target_node.data = target_node.next.data
    target_node.next = target_node.next.next

    return llist


if __name__ == "__main__":
    print(delete_middle(target_node))