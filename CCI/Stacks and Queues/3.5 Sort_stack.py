class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.stack_sorted = []
    
    def __repr__(self) -> str:
        arr1 = []
        arr2 = []
        for value in self.stack:
            arr1.append(value)
        for value in self.stack_sorted:
            arr2.append(value)
        return str([arr1, arr2])
    
    def is_empty(self, stack):
        return len(stack) == 0
    
    def peek(self, stack):
        return stack[-1]
        

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def sort(self):
        while self.is_empty(self.stack) == False:
            temp = self.stack.pop()
            while self.is_empty(self.stack_sorted) != True and self.stack_sorted[-1] <= temp:
                self.stack.append(self.stack_sorted.pop())
        
            self.stack_sorted.append(temp)

            #to decrease number of iterations it can have another while loop moving from stack to stack_sorted all previously moved pieces,
            #as they are chronocly ordered. Use counter to check number or moved numbers or add condition for increasing numbers

            print(temp)
            print(self.stack)
            print(self.stack_sorted)
            print(f"{self.peek(self.stack_sorted)}, {len(self.stack_sorted) == 0}")


if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(6)
    print(stack)
    stack.sort()
    print(stack)

