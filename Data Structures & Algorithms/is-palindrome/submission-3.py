class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # new_Str = ''
        # for char in s:
        #     if char.isalnum():
        #         new_Str += char
        
        # if new_Str == new_Str[::-1]:
        #     return True
        # else:
        #     return False
    
        l, r = 0 , len(s) - 1
        
        while l < r:
            if not s[r].isalnum():
                r -= 1
                continue
            if not s[l].isalnum():
                l += 1
                continue
            if s[l].lower() != s[r].lower():
                return False 
            l += 1
            r -= 1

        return True
        
        

                    