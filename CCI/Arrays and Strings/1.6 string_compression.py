input = 'aaaaBzadzBh'
#input = 'aabcccccaaa'

def string_copression(input: str) -> str:
    i,count = 1,1
    string,charf ='', ''
    string += input[0]
    charf = string[0]

    while len(string) < len(input) and i < len(input):
        
        if input[i] == charf:
            count +=1
          #  print("if", input[i], " ",count)

        else:
            string += str(count) + input[i]
          #  print(string)
            count = 1
            charf = input[i]
           # print(input[i])

            
        i+=1

    string += str(count)
    if len( string) >  len(input):
        return input
    return string

if __name__ == "__main__":
    print(string_copression(input))