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
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data
    

llist_1 = LinkedList()
l1_node1 = Node(7)
llist_1.head = l1_node1
l1_node2 = Node(1)
l1_node1.next = l1_node2
l1_node3 = Node(6)
l1_node2.next = l1_node3
l1_node4 = Node(1)
l1_node3.next = l1_node4

llist_2 = LinkedList()
l2_node1 = Node(5)
llist_2.head = l2_node1
l2_node2 = Node(9)
l2_node1.next = l2_node2
l2_node3 = Node(2)
l2_node2.next = l2_node3


##tranfsormint to int
def translate_to_number(linked_list):
    number = 0
    i=0
    node = linked_list.head
    
    while node is not None:
        number += node.data * 10**i
        i += 1
        node = node.next
    return number

def translate_to_list(number, output_list):
    number = str(number)
    node = Node(0)
    output_list.head = node
    for char in reversed(number):
        node.next = Node(int(char))
        node = node.next
    
    output_list.head = output_list.head.next
    return output_list
    

def sum_lists_back(llist_1, llist_2):
    output = LinkedList()
    number1 = translate_to_number(llist_1)
    number2 = translate_to_number(llist_2)
    sum = number1+number2

    return translate_to_list(sum, output)


## all linked list  iterated simultaniously
def sum_list(llist_1, llist_2):
    output = LinkedList()
    node_output = Node(0)
    output.head = node_output
    node1 = llist_1.head
    node2 =llist_2.head
    value_next = 0

    while True:
        if node1 is None:
            node1 = Node(0)
        if node2 is None:
            node2 = Node(0)
        if node1.data == 0 and node2.data == 0:
            break

        temp = node1.data + node2.data
        if temp >= 10:
            value = temp % 10
            node_output.next = Node(value + value_next)
            value_next = temp // 10
        else:
            node_output.next = Node(temp+value_next)
            value_next = 0
            
        node_output = node_output.next
        node1 = node1.next
        node2 = node2.next

    output.head =  output.head.next
    return output


print(sum_lists_back(llist_1,llist_2))
print(sum_list(llist_1, llist_2))