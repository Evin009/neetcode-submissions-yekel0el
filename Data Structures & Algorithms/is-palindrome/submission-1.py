class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_Str = ''
        for char in s:
            if char.isalnum():
                new_Str += char
        
        if new_Str == new_Str[::-1]:
            return True
        else:
            return False