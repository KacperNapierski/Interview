class MyQueue:
    def __init__(self) -> None:
        self.stack_in = []
        self.stack_out = []
    
    def __repr__(self) -> None:
        arr1 = []
        arr2 = []
        for value in self.stack_in:
            arr1.append(value)
        for value in self.stack_out:
            arr2.append(value)

        return str([arr1, arr2])
    
    def _is_empty(self, stack) -> bool:
        return len(stack) == 0
    
    def _move(self, source, destination):
        while self._is_empty(source) == False:
            destination.append(source.pop())

    def push(self, value):
        if len(self.stack_out) != 0:
            self._move(self.stack_out, self.stack_in)
        self.stack_in.append(value)
    
    def pop(self):
        self._move(self.stack_in, self.stack_out)
        self.stack_out.pop()

if __name__ == "__main__":

    queue = MyQueue()
    print(queue)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue)
    queue.pop()
    print(queue)
    queue.push(5)
    print(queue)
    queue.pop()
    print(queue)
