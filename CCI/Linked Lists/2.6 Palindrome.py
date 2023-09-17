class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __rep__(self) -> list:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node)
            node = node.next
        return nodes

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data
    

llist = LinkedList()
node1 = Node('t')
llist.head = node1
node2 = Node('e')
node1.next = node2
node3 = Node('n')
node2.next = node3
node4 = Node('e')
node3.next = node4
node5 = Node('t')
node4.next = node5

###STACK
def is_palindrome_stack(llist)->bool:
    stack = []
    node = llist.head

    while node is not None:
        stack.append(node.data)
        node = node.next

    while llist.head is not None:
        if stack[-1] != llist.head.data: return False
        stack.pop()
        llist.head = llist.head.next

    if len(stack) == 0:
        return True


###REVERSE
def reverse_and_clone(node)->LinkedList:
    linked_list = LinkedList()
    linked_list.head = None
    head = linked_list.head
    while node is not None:
        new_node = Node(node.data)
        new_node.next = head
        head = new_node
        node = node.next
    return head

def is_palindrome_reversed(llist)->bool:
    node = llist.head
    reversed_node = reverse_and_clone(node)
    while (node is not None) and (reversed_node is not None):
        if node.data != reversed_node.data: return False
        node = node.next
        reversed_node = reversed_node.next
    
    return node == None and reversed_node == None



if __name__ == '__main__':
    #print(is_palindrome_stack(llist))
    print(is_palindrome_reversed(llist))