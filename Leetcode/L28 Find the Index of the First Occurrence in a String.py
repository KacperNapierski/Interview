haystack = "mississippi"
needle = "issip"
i=0
j=0
k = 0
index=0
if needle == "":
    print(-1)
    
for i in range(len(haystack)):
            print(f"k = {k}, j = {j}, haystack = {haystack[k]}, needle = { needle[j]}")
            if j == len( needle):
                index = i-len(needle)
                print("Done")
            if haystack[k] == needle[j]:
                j+=1
            else:
                if(j>0):
                    k -=(j-1)
                j=0
            k+=1


if j == len( needle):
    index = len(haystack)-len(needle)
    print(index)          
print(-1)