class Solution:
    def isValid(self, s: str) -> bool:

        dict = {"(":")", "{":"}", "[":"]"}
        stack =[]

        for char in s:
            if char in dict:
                stack.append(char)
            
            elif len(stack)==0 or char != dict[stack.pop()]:
                return False
            
        return len(stack)==0

#65 ms, faster than 25.70%
#13.9 MB, less than 72.24%