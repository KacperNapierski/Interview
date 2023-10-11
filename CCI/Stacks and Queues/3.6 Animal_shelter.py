class Node:
    def __init__(self,type) -> None:
        self.type = type
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = self.tail = None

    def __repr__(self) -> str:
        node = self.front
        nodes = []
        while node is not None:
            nodes.append(node.type)
            node = node.next
        return str(nodes)
    
    def isEmpty(self):
        return self.front == None
    
    def enqueue(self, type):
        node = Node(type)
        if self.tail == None:
            self.front = self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def dequeueAny(self):
        if self.isEmpty():
            return
        
        self.front = self.front.next
        if self.front == None:
            self.tail = None

    def dequeueDog(self):
        if self.isEmpty():
            return
        if self.front.type == 'dog':
            self.front = self.front.next
            return

        node = self.front
        while node.next is not None:
            if node.next.type == 'dog':
                node.next = node.next.next
                return
            node = node.next

    def dequeueCat(self):
        if self.isEmpty():
            return
        if self.front.type == 'cat':
            self.front = self.front.next
            return

        node = self.front
        while node.next is not None:
            if node.next.type == 'cat':
                node.next = node.next.next
                return
            node = node.next



if __name__ == '__main__':
    queue = Queue()
    print(queue)
    queue.enqueue("cat")
    queue.enqueue("dog")
    queue.enqueue("cat")
    queue.enqueue("dog")
    print(queue)
    queue.dequeueAny()
    print(queue)
    queue.dequeueDog()
    print(queue)
    queue.dequeueDog()
    print(queue)
    queue.dequeueAny()
    print(queue)
    print('###')
    queue.enqueue("cat")
    print(queue)
    queue.dequeueDog()
    print(queue)
    queue.enqueue("dog")
    queue.enqueue("cat")
    queue.dequeueDog()
    print(queue)
    queue.enqueue("dog")
    queue.enqueue("cat")
    queue.dequeueAny()
    print(queue)
    queue.enqueue("dog")
    queue.enqueue("cat")
    queue.dequeueCat()
    print(queue)
    queue.enqueue("dog")
    queue.dequeueAny()
    print(queue)


