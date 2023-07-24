class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            
            if char == ")":
                try:
                    if stack.pop() == "(":
                        continue
                except:
                    return False

                else:
                    return False
            
            if char == "}":
                try:
                    if stack.pop() == "{":
                        continue
                except:
                    return False

                else:
                    return False

            if char == "]":
                try:
                    if stack.pop() == "[":
                        continue
                except:
                    return False

                else:
                    return False

        if len(stack) == 0:
            return True
        
        else:
            return False

#38 ms, faster than 84.31%
#14 MB, less than 26.40%