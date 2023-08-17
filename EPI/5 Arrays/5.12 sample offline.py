from random import randint

input = [5, 10, 4, 12,3] #0-4
k = 3

def sample_data(input:list, k:int) -> list:
    
    for i in range (k): #0-2
        random = randint(i,len(input)-1)
        input[i], input[random] = input[random], input[i]

    return input[:k]

if __name__ == '__main__':
    print(sample_data(input,k))
