class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = set()
        output = []

        for i in range(len(nums)):
            if (target - nums[i]) in hashset:
                output.append(i)
                output.append(nums.index(target - nums[i]))
                return output
            
            hashset.add(nums[i])

