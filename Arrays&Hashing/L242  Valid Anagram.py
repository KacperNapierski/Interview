class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def sortedString(string):
            string = ''.join(sorted(string))
            return string
        
        if sortedString(s) == sortedString(t):
            return True
        
        return False