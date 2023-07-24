input = "Mr John Smith   "
true_lenght=13
#input = ""

## Join method
#def insert_url(input: str) -> str:
#    if len(input)>0:
#        input = input.split()
#        input = "%20".join(input)
#        return input
#    return 0

## Brute Force
#def countofChar(string: str, start: int, end: int, target: int) -> int:
#    count = 0
#    for i in range(start, end):
#        if string[i] == target:
#            count +=1
#    return count
#
#def insert_url(input: str, k: str) -> str:
#    number_of_spaces = countofChar(input, 0, true_lenght, " ")
#    newIndex = true_lenght -1 + number_of_spaces*2
#
#    if (newIndex +1 < len(input)):
#        input[newIndex +1] = '\0'
#    
#    for oldIndex in range(true_lenght -1, 0, -1):
#        if input[oldIndex] == ' ':
#            input[newIndex] = '0'
#            input[newIndex -1] = '2'
#            input[newIndex -2] = "%"
#            newIndex -=3
#        else:
#            input[newIndex]= input[oldIndex]
#            newIndex -=1
#
#    return 


def insert_url(input: str, true_lenght: str) -> str:
    output = ""

    for i in range(true_lenght):
        if input[i] == " ":
            output += "%20"
        else:
            output += input[i]
    return output

if __name__ == '__main__':
    print(insert_url(input,true_lenght))