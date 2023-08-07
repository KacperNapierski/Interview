#input = [310,315,275,295,260,270,290,230,255,250]
input = [10,12,15,11,4,5,7,11,11,24]

def stock_once(input:list) -> int:
    minimum, maximum, profit = input[0], 0, 0

    for i in range(1, len(input)):
        if input[i] < minimum:
            minimum = input[i]
            maximum = 0
        if input[i] > maximum:
            maximum = input[i]
            if maximum - minimum > profit:
                profit = maximum - minimum

    return profit

if __name__ == "__main__":
    print(stock_once(input))