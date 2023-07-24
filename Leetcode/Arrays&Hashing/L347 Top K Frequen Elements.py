class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = set()
        freq = []

        for num in nums:
            if num in hashset:
                freq[num] +=1
                hashset.add(num)
        
        
