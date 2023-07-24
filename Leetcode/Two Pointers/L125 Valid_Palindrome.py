class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(letter for letter in s if letter.isalnum())

        if string.lower() == string[::-1].lower():
            return True

        else:
            return False

## 66ms faster than 80.48%
## 14.7 mb less than 35.57%