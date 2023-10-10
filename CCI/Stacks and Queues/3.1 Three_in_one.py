NUMBER_OF_STACKS = 3
# stack_number 0-3

class KStacks:
    def __init__(self, number_of_stacks) -> None:
        self.number_of_stacks = number_of_stacks
        self.array = [0] * number_of_stacks
        self.stack_top = [i for i in range(number_of_stacks)] #[0,1,2]

    def __repr__(self) -> str:
        arr = []
        for value in self.array:
            arr.append(value)
        return str(arr)

    def push(self, item, stack_number):
        print('#########')

        for index in range(len(self.stack_top[stack_number:])):
            self.stack_top[stack_number+index] += 1
        self.array.insert(self.stack_top[stack_number], item)

    def pop(self, stack_number):
        self.array.pop(self.stack_top[stack_number])
        for index in range(len(self.stack_top[stack_number:])):
            self.stack_top[stack_number+index] -= 1


if __name__ == "__main__":
    kstack = KStacks(NUMBER_OF_STACKS)
    print(kstack)
    kstack.push(1,0)
    print(kstack)
    kstack.push(11,1)
    print(kstack)
    kstack.push(2,0)
    print(kstack)
    kstack.push(12,1)
    print(kstack)
    kstack.push(3,0)
    kstack.push(13,1)
    kstack.push(4,0)
    kstack.push(5,0)
    kstack.push(21,2)
    kstack.push(22,2)
    kstack.push(6,0)
    kstack.push(14,1)
    print(kstack)
    kstack.pop(1)
    kstack.pop(0)


    print(kstack)
    


    

        