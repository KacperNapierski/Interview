x=1000021
x = str(x)
for i in range(len(x)):
    if x[i] != x[-i-1]:
        print(False)
    
print(True)