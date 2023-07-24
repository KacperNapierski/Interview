nums= [0,1,2,2,3,0,4,2]
val=2

j = 0
i=0
while i<len(nums):
    print(i)
    if nums[i] == val:
        j+=1
        nums.remove(nums[i])
    else:
        i+=1
    
print(len(nums)-j)
print(nums)