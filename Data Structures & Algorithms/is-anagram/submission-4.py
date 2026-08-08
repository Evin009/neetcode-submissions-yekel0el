class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            # creates two arrays 
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        # if anagram count should be zero for all 26 spaces

        for val in count:
            if val != 0:
                return False
        
        return True