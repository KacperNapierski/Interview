class SetOfStacks:
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.array = []
        self.number_of_stacks = 1
        self.stack_top = [0]

    def __repr__(self) -> str:
        arr = []
        for value in self.array:
            arr.append(value)
        return str(arr)
    
    def is_full(self) -> bool:
        if self.stack_top[self.number_of_stacks-1] == self.max_size*self.number_of_stacks:
            return True
        return False
    
    def is_empty(self):
        if self.stack_top[self.number_of_stacks-1]%self.max_size == 0:
            return True
        return False

    def top(self):
        print(self.array[-1])
        return self.array[-1]
    
    def push(self, value):
        #check if full
        # if full -> new number of stacks
        print('######PUSH#######')

        if self.is_full() == True:
            #creater new stack
            self.stack_top.append(self.stack_top[self.number_of_stacks-1]) #+1
            self.number_of_stacks += 1
        self.array.append(value)
        self.stack_top[self.number_of_stacks-1] += 1

    def pop(self):
        # check if empty then return top from previous stack
        print('######POP#######')
        self.array.pop()
        self.stack_top[self.number_of_stacks-1] -= 1
        if self.is_empty() == True:
            self.stack_top.pop()
            self.number_of_stacks -= 1


if __name__ == '__main__':
    stacks = SetOfStacks(3)

    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.push(1)
    stacks.push(2)
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.push(3)
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.push(4)
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.push(5)
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.pop()
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.pop()
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.push(5)
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.push(5)
    stacks.push(5)
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.push(5)
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.push(5)
    stacks.push(5)
    stacks.push(5)
    stacks.push(5)
    stacks.push(5)
    stacks.push(5)
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    print(stacks.stack_top)
    print(stacks.number_of_stacks)
    print(stacks)

    

        