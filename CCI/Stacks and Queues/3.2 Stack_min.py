class Stack:
    def __init__(self) -> None:
        self.array = []
        self.min_values = []
    
    def __repr__(self) -> str:
        return str(self.array)
    
    def push(self, value) -> None:
        self.array.append(value)

        if len(self.min_values) == 0:
            self.min_values.append(value)
        elif value <= self.min_values[-1]:
            self.min_values.append(value) 

    def pop(self) -> None:
        if self.array[-1] == self.min_values[-1]: ###
            self.min_values.pop()
        self.array.pop()

    def top(self) -> int:
        return self.array[-1]
    
    def min(self) -> int:
        print(self.min_values[-1])
        return self.min_values[-1]
    
if __name__ == '__main__':

    stack = Stack()
    print(stack)

    stack.push(5)
    stack.push(4)
    stack.push(6)
    stack.push(2)
    print(stack)
    stack.min()
    stack.pop()
    stack.push(3)
    print(stack)
    stack.min()

    stack.pop()
    stack.pop()
    stack.pop()
    stack.min()



