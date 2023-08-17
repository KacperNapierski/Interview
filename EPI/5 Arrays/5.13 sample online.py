from random import randrange

input = [5,3,4,10,15,18,33,19,2]
k = 2


def sample_offline(input:list, k:int) -> list:
    num_so_far = k

    for x in input:
        num_so_far +=1
        index = randrange(num_so_far)
        if index < k:
            input[index] = x

    return input[:k]

if __name__ == '__main__':
    print(sample_offline(input,k))
