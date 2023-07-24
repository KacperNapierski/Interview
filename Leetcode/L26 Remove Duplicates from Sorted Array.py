nums = [0,0,1,1,1,2,2,3,3,4]

#myset = set()
#for num in nums:
#    if num in myset:
#        continue
#    else:
#        myset.add(num)
#print(nums)
#nums = list(myset)
#print(myset)
#print(nums)
#print(len(myset))


myset = set()
for i in range(len(nums)):
    print(myset)
    print(nums)
    if nums[i] in myset:
        nums.remove(nums[i])
        nums.insert(-1,nums[i])
    else:
        myset.add(nums[i])

    print(myset)
    print(nums)


print(len(myset))