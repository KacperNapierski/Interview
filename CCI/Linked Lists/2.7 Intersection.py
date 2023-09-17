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
    
llist1 = LinkedList()
llist2 = LinkedList()
node11 = Node(2)
llist1.head = node11
node12 = Node(5)
node11.next = node12
node13 = Node(6)
node12.next = node13

node21 = Node(3)
llist2.head = node21
node22 = Node(4)
node21.next = node22

node1 = Node(7)
node13.next = node1
node22.next = node1

node2 = Node(2)
node1.next = node2
node3 = Node(1)
node2.next = node3


###BruteForce
def intersection_iter(llist1, llist2):
   for node1 in llist1:
       for node2 in llist2:
           if node1.next == node2.next:
               return node1.next
           
def intersection_brute_force(llist1,llist2):
    node1 = llist1.head
    while node1 is not None:
        node2 = llist2.head
        while node2 is not None:
            if node1.next == node2.next:
                return node1.next
            node2 = node2.next
        node1 = node1.next

### Visited mark
def intersection_visited(llist1,llist2):
    node1 = llist1.head
    while node1 is not None:
        node1.visited = True
        node1 = node1.next
    node2 =llist2.head
    while node2 is not None:
        if node2.visited == True:
            return node2
        node2 = node2.next

### 

def get_len(llist):
    count = 0
    for node in llist:
        count +=1
    return count

def get_intersection_node(len_difference, llist1, llist2):
    node1 = llist1.head #longer
    node2 = llist2.head

    #equaling the tails of the lists
    for _ in range(len_difference):
        if node1 is None: return False
        node1 = node1.next

    while (node1 is not None) and (node2 is not None):
        if node1 == node2:
            return node1
        node1 = node1.next
        node2 = node2.next
    return False

def intersection(llist1, llist2):
    len_list1 = get_len(llist1)
    len_list2 = get_len(llist2)
    len_difference = abs(len_list1 - len_list2)

    if len_list1 > len_list2:
        return get_intersection_node(len_difference,llist1, llist2)
    else:
        return get_intersection_node(len_difference,llist2, llist1)


#print(intersection_iter(llist1, llist2))
#print(intersection_brute_force(llist1, llist2))
#print(intersection_visited(llist1, llist2))
print(intersection(llist1, llist2))